#!/usr/bin/env python3
"""Compile the checked-in proof compilation twice, retaining XeLaTeX diagnostics."""
from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parents[1]
dest=root/'build'/'proofs';dest.mkdir(parents=True,exist_ok=True)
for n in (1,2):
    p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={dest}','proofs/all-proofs.tex'],cwd=root,capture_output=True,text=True)
    (dest/f'pass-{n}.txt').write_text(p.stdout+p.stderr)
    if p.returncode:raise SystemExit(p.stdout[-5000:])
shutil.copy2(dest/'all-proofs.pdf',root/'pdf'/'gpt-All-Proofs.pdf')
print('Built pdf/gpt-All-Proofs.pdf')
