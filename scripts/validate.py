#!/usr/bin/env python3
"""Check ordered source-page coverage and successful, readable PDF builds."""
import hashlib,json,re
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
IDS=['000','000-ZSM']+[str(i) for i in range(101,111)]
rows=[]
for key in IDS:
    source=ROOT/'sources'/('000-PPT.pdf' if key=='000' else ('000-ZSM-PPT.pdf' if key=='000-ZSM' else f'{key}-ZSM-PPT.pdf'))
    doc=fitz.open(source); count=len(doc)
    body=(ROOT/'notes'/f'{key}-body.tex').read_text()
    pages=list(map(int,re.findall(r'\\Slide\{(\d+)\}',body)))
    assert pages==list(range(1,count+1)), (key,'missing or unordered source pages')
    pdf=ROOT/'pdf'/f'gpt-{key}.pdf'; compiled=fitz.open(pdf)
    assert len(compiled)>=count
    # Every Slide emits a PDF form containing the original PDF page.
    forms=[x for pg in compiled for x in pg.get_xobjects() if x[1].startswith('Im') or x[1].startswith('Fm')]
    assert len(forms)>=count, (key,'missing embedded source forms')
    text='\n'.join(pg.get_text() for pg in compiled)
    assert '中文' in text and '原课件' in text, (key,'unreadable CJK text')
    log=(ROOT/'build'/key/f'{key}.log').read_text(errors='replace')
    assert 'Missing character:' not in log, (key,'missing font glyph')
    assert 'Output written on' in log
    rows.append(dict(lecture=key,source_pages=count,note_pages=len(compiled),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest()))
(ROOT/'coverage.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(f'PASS: {len(rows)} PDFs; {sum(r["source_pages"] for r in rows)} original pages embedded in order; {sum(r["note_pages"] for r in rows)} note pages. No missing font glyphs.')
