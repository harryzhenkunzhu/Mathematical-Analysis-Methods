#!/usr/bin/env python3
"""Compile standalone manuscripts, check output, merge volumes and package ZIP."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess, shutil, json, zipfile, hashlib
import fitz
HERE=Path(__file__).resolve().parent
BUILD=HERE/'build'; BUILD.mkdir(exist_ok=True)
PDF=HERE/'pdf'; PDF.mkdir(exist_ok=True)
def compile_one(lec):
 for _ in range(3):
  result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',
   '-output-directory=../build',f'gpt-{lec}-exam.tex'],cwd=HERE/'latex',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (BUILD/f'compile-{lec}.txt').write_bytes(result.stdout)
  if result.returncode:raise RuntimeError(result.stdout[-3000:].decode(errors='replace'))
 log=(BUILD/f'gpt-{lec}-exam.log').read_text()
 for bad in ['Overfull','Missing character:','undefined references','Label(s) may have changed']:
  if bad in log:raise RuntimeError(f'{lec}: unresolved compilation issue: {bad}')
 src=BUILD/f'gpt-{lec}-exam.pdf'; dst=PDF/src.name; shutil.copy(src,dst)
 doc=fitz.open(dst)
 text='\n'.join(p.get_text() for p in doc)
 assert '原课件逐页对应索引' in text and len(text)>35000
 assert not any(p.get_images() for p in doc), 'Raster screenshot unexpectedly present'
 return lec,{'pdf_pages':len(doc),'extracted_characters':len(text),'bytes':dst.stat().st_size,
             'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'compile_checks':'passed'}
report=dict(ThreadPoolExecutor(2).map(compile_one,['108','109']))
# Compile a genuine single LaTeX document. Concatenating two standalone PDFs
# retains two unrelated internal contents pages, not a unified printed TOC.
def compile_combined():
 for _ in range(3):
  result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',
   '-output-directory=../build','gpt-108-109-exam.tex'],
   cwd=HERE/'latex',stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (BUILD/'compile-108-109.txt').write_bytes(result.stdout)
  if result.returncode:
   raise RuntimeError(result.stdout[-4000:].decode(errors='replace'))
 log=(BUILD/'gpt-108-109-exam.log').read_text()
 for bad in ['Overfull','Missing character:','undefined references','Label(s) may have changed']:
  if bad in log:raise RuntimeError(f'108-109: unresolved compilation issue: {bad}')
 src=BUILD/'gpt-108-109-exam.pdf'
 dst=PDF/src.name
 shutil.copy(src,dst)
 doc=fitz.open(dst)
 toc=doc.get_toc()
 titles=[title for level,title,page in toc]
 p108=next((page for level,title,page in toc if 'Lecture 108' in title),None)
 p109=next((page for level,title,page in toc if 'Lecture 109' in title),None)
 assert p108 is not None and p109 is not None and p108 < p109, \
  'Unified PDF bookmarks must contain both lectures in order'
 contents_text='\n'.join(doc[i].get_text() for i in range(min(7,len(doc))))
 assert 'Lecture 108' in contents_text and 'Lecture 109' in contents_text, \
  'Both lectures must appear in the front printed table of contents'
 assert '原课件逐页对应索引' in '\n'.join(p.get_text() for p in doc)
 assert len(doc)>70 and not any(p.get_images() for p in doc)
 return {'pages':len(doc),'lecture_108_starts':p108,'lecture_109_starts':p109,
  'toc_entries':len(toc),'bytes':dst.stat().st_size,
  'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),
  'compile_checks':'passed','unified_printed_toc':'both lectures confirmed'}

joint=compile_combined()
report['combined_pages']=joint['pages']
report['combined_toc']=joint
(HERE/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
archive=HERE.parent/'downloads/gpt-108-109-exam.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in [HERE/'README.md',HERE/'coverage.json',HERE/'validation.json',*sorted((HERE/'latex').glob('*.tex')),*sorted(PDF.glob('*.pdf'))]:
  z.write(p,Path('gpt-108-109-exam')/p.relative_to(HERE))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps(report,ensure_ascii=False,indent=2));print('ZIP:',archive.stat().st_size,'bytes')
