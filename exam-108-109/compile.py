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
combined=fitz.open(); toc=[]
for lec in ['108','109']:
 doc=fitz.open(PDF/f'gpt-{lec}-exam.pdf'); offset=len(combined)
 toc.append([1,f'Lecture {lec}',offset+1])
 toc.extend([[level+1,title,page+offset] for level,title,page in doc.get_toc()])
 combined.insert_pdf(doc)
combined.set_toc(toc)
combined.set_metadata({'title':'108与109：证明考试中文自学讲义','author':'中文自学讲义'})
combined.save(PDF/'gpt-108-109-exam.pdf',garbage=4,deflate=True)
report['combined_pages']=len(combined)
(HERE/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
archive=HERE.parent/'downloads/gpt-108-109-exam.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in [HERE/'README.md',HERE/'coverage.json',HERE/'validation.json',*sorted((HERE/'latex').glob('*.tex')),*sorted(PDF.glob('*.pdf'))]:
  z.write(p,Path('gpt-108-109-exam')/p.relative_to(HERE))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps(report,ensure_ascii=False,indent=2));print('ZIP:',archive.stat().st_size,'bytes')
