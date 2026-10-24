#!/usr/bin/env python3
"""Build all twelve notes with XeLaTeX, retaining diagnostics in build/."""
from pathlib import Path
import argparse, concurrent.futures, subprocess
ROOT = Path(__file__).resolve().parents[1]
IDS = ['000', '000-ZSM', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110']
def build(key):
    dest = ROOT/'build'/key
    dest.mkdir(parents=True, exist_ok=True)
    for turn in range(2):
        result = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', f'-output-directory={dest}', f'notes/{key}.tex'], cwd=ROOT, capture_output=True, text=True)
        (dest/f'pass-{turn+1}.txt').write_text(result.stdout + result.stderr)
        if result.returncode:
            return key, False, (result.stdout + result.stderr)[-5000:]
    (ROOT/'pdf').mkdir(exist_ok=True)
    import shutil
    shutil.copy2(dest/f'{key}.pdf', ROOT/'pdf'/f'gpt-{key}.pdf')
    return key, True, ''
if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('ids', nargs='*'); parser.add_argument('-j',type=int,default=3); args=parser.parse_args()
    selected=args.ids or IDS
    if any(x not in IDS for x in selected): parser.error('unknown lecture ID')
    good=True
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.j) as pool:
        for key, ok, output in pool.map(build, selected):
            print(key, 'OK' if ok else 'FAILED', output, flush=True); good &= ok
    raise SystemExit(0 if good else 1)
