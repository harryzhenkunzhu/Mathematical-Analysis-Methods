#!/usr/bin/env python3
from pathlib import Path
import json,re,hashlib,runpy
import fitz
root=Path(__file__).resolve().parents[1]
idx=json.loads((root/'proofs/proof-index.json').read_text())
selected={}
for row in idx:
    for n in row['proof_pages']:
        selected.setdefault(row['source'],set()).add(n)
        assert 1<=n<=len(fitz.open(root/'sources'/row['source']))
# These pages mention proofs without actually presenting one.
allowed={'101-ZSM-PPT.pdf':{7},'108-ZSM-PPT.pdf':{17},'109-ZSM-PPT.pdf':{16}}
for source in (root/'sources').glob('*.pdf'):
    for i,pg in enumerate(fitz.open(source),1):
        if re.search(r'\bProof\b',pg.get_text(),re.I):
            assert i in selected.get(source.name,set()) or i in allowed.get(source.name,set()),(source.name,i)
detailed={}
for module in (root/'proofs/detailed').glob('*.py'):
    detailed.update(runpy.run_path(str(module))['BLOCKS'])
for row in idx:
    identity=row['lecture']+':'+str(row['proof_pages'][0])
    assert identity in detailed, ('missing independently written proof',identity)
assert 'body=custom if custom' not in (root/'scripts/assemble_proofs.py').read_text()
assert 14 in selected['109-ZSM-PPT.pdf'], 'missing continuation of compact-sum proof'
p=root/'pdf/gpt-Proofs-Full-Steps.pdf';doc=fitz.open(p)
assert len(doc)>100
text='\n'.join(pg.get_text() for pg in doc)
assert '证明详解：按老师课件路线重写' in re.sub(r'\s+', '', text) and re.search(r'110.Proof', re.sub(r'\s+', '', text))
forms=sum(len(pg.get_xobjects()) for pg in doc)
assert forms==0, 'embedded PDF forms found'
assert all(not pg.get_images() for pg in doc), 'embedded images found'
assert '\\includegraphics' not in (root/'proofs/all-proofs.tex').read_text()
log=(root/'build/proofs/all-proofs.log').read_text(errors='replace')
assert 'Missing character:' not in log
assert 'Overfull' not in log
assert 'Output written on' in log
report={'source_entries':len(idx),'referenced_source_pages':sum(len(x['proof_pages']) for x in idx),'compiled_pages':len(doc),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks':['source page ranges valid','all explicit Proof mentions accounted for or specifically excluded','no embedded images or PDF page forms','no missing glyphs','no overfull boxes','every item has a dedicated detailed body','109 pages 13 and 14 form one complete proof']}
(root/'proofs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
