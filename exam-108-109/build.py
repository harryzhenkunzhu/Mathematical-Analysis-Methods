#!/usr/bin/env python3
"""Assemble standalone Chinese manuscripts with explicit teacher-page coverage."""
from pathlib import Path
import re, json, runpy, hashlib, shutil
ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
CFG=runpy.run_path(str(HERE/'chapters/content.py'))
SUP=runpy.run_path(str(HERE/'chapters/supplements.py'))['SUPPLEMENTS']
STATEMENTS=json.loads((ROOT/'proofs/statements.json').read_text())
INDEX=json.loads((ROOT/'proofs/proof-index.json').read_text())
OUT=HERE/'latex'; OUT.mkdir(exist_ok=True)
shutil.copy(HERE/'chapters/foundations.tex',OUT/'foundations.tex')
PRE=r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=21mm,headheight=17pt]{geometry}
\usepackage{fontspec}
\setmainfont[AutoFakeSlant=.18]{Noto Serif CJK SC}
\setsansfont{Noto Sans CJK SC}
\setmonofont{Noto Sans Mono CJK SC}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip=0pt plus 1pt
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{xcolor,enumitem,fancyhdr,longtable,booktabs,needspace,tikz}
\usepackage[unicode,colorlinks=true,linkcolor=blue!55!black,urlcolor=blue!55!black]{hyperref}
\newcommand{\R}{\mathbb{R}}\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}\newcommand{\Z}{\mathbb{Z}}
\newcommand{\eps}{\varepsilon}
\newcommand{\norm}[1]{\left\lVert#1\right\rVert}
\newcommand{\abs}[1]{\left\lvert#1\right\rvert}
\DeclareMathOperator{\conv}{co}\DeclareMathOperator{\cl}{cl}
\DeclareMathOperator{\Int}{int}\DeclareMathOperator{\diam}{diam}
\DeclareMathOperator{\dist}{dist}
\newtheorem{theorem}{定理}\newtheorem{lemma}{引理}
\newtheorem{proposition}{命题}
\theoremstyle{definition}\newtheorem{definition}{定义}\newtheorem{example}{例}
\renewcommand{\proofname}{证明}
\setlength{\parindent}{0pt}\setlength{\parskip}{.5em}\linespread{1.18}
\setlist{itemsep=3pt,topsep=4pt,leftmargin=2em}
\emergencystretch=4em\setcounter{tocdepth}{1}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small 数理分析方法 · 证明考试自学讲义}
\fancyhead[R]{\small Lecture \LectureID}
\fancyfoot[C]{\thepage}
'''
(OUT/'preamble.tex').write_text(PRE)
# Keep explanatory definitions/examples from previous author text, not its screenshot
# macros or placeholder pages. Proofs come from the fully expanded source below.
KEEP={
'108':{1,2,3,4,5,6,7,8,9,10,13,15,16,17,18,22},
'109':{1,2,3,4,5,6,7,8,9,15,16,18,19,20,21,22,24,26,27,28,30,34,37,42,46,48,55,60,67,76,81,84,88,92,97,104,109,114}
}
# Several proof units are deliberately repeated in the teacher's second exposition.
# Adjacent identical variants are combined while preserving every source-page tag.
manifest={}
for lec,mod,total in [('108','correspondences',113),('109','vectors',118)]:
 blocks=runpy.run_path(str(ROOT/f'proofs/detailed/{mod}.py'))['BLOCKS']
 old=(ROOT/f'notes/{lec}-body.tex').read_text()
 parts=re.split(r'\\Slide\{(\d+)\}\{([^\n]+)\}\n',old)
 notes={int(parts[i]):(parts[i+1],parts[i+2]) for i in range(1,len(parts),3)}
 entries=[e for e in INDEX if e['lecture']==lec]
 covered=[]; proofcovered=[]; rendered=[]; body=[]
 for start,end,title in CFG['GROUPS'][lec]:
  label=f'g:{lec}:{start}'
  body.append(r'\clearpage\section{'+title+'}'+r'\label{'+label+'}')
  body.append(r'\textbf{对应原课件：'+lec+'，第 '+str(start)+(('--'+str(end)) if end!=start else '')+r' 页。}')
  covered.extend(range(start,end+1))
  body.append(CFG['EXTRA'].get((lec,start),''))
  for p in range(start,end+1):
   if p in KEEP[lec] and f'{lec}:{p}' not in blocks:
    title0,text=notes[p]
    assert '见本讲' not in text
    # Remove obsolete delivery claims, never include the old screenshot caption.
    text=text.split(r'\section*{')[0]
    body.append(r'\paragraph{原页'+str(p)+'：'+title0+'。}'+text)
  units={}
  for e in entries:
   p=e['proof_pages'][0]
   if start<=p<=end:
    key=f'{lec}:{p}'; content=blocks[key]
    units.setdefault(content,[]).append(e)
    proofcovered.extend(e['proof_pages'])
  for content,es in units.items():
   pages=sorted({p for e in es for p in e['proof_pages']})
   p=es[0]['proof_pages'][0]; key=f'{lec}:{p}'
   st=STATEMENTS[key]
   tags='、'.join(map(str,pages))
   body.append(r'\subsection{命题与证明：原页 '+tags+'}')
   body.append(r'\textbf{命题。}'+st['statement'])
   body.append(r'\paragraph{老师的证明思路。}'+st['idea'])
   body.append(r'\paragraph{逐步推导。}'+content)
   for e in es:
    extra=SUP.get((lec,e['proof_pages'][0]),'')
    if extra:body.append(extra)
   rendered.append({'source_pages':pages,'section':title,'key':key})
  # Teacher page63 has a statement but no proof: clearly marked added proof.
  if lec=='109' and start<=63<=end: body.append(SUP[('109',63)])
 assert covered==list(range(1,total+1)),(lec,covered)
 assert sorted(proofcovered)==sorted(p for e in entries for p in e['proof_pages'])
 body.append((HERE/f'chapters/exercises{lec}.tex').read_text())
 body.append(r'\clearpage\section{原课件逐页对应索引}')
 body.append('下表每行是一张教师原课件页。续页、重复页及图示页随所在专题合并解释；新讲义页码指该专题的开始位置，具体证明另在正文标出原页。')
 body.append(r'\begin{longtable}{r p{.66\linewidth} r}\toprule 原课件页&本讲义对应专题&本讲义页\\\midrule\endhead')
 for start,end,title in CFG['GROUPS'][lec]:
  for p in range(start,end+1):
   body.append(str(p)+' & '+title+r' & \pageref{g:'+lec+':'+str(start)+r'}\\')
 body.append(r'\bottomrule\end{longtable}')
 body.append(r'\paragraph{材料与记号说明。}按用户提供的教师原课件 '+lec+'-ZSM-PPT.pdf 重新编写；相关基础背景参照 Debreu 的 Theory of Value。正文以教师原页为定位，不以旧 gpt 笔记分页为定位。补充证明与原稿纠正均显式说明。')
 manuscript='\n\n'.join(body)
 assert r'\includegraphics' not in manuscript and '见本讲原页' not in manuscript
 (OUT/f'body-{lec}.tex').write_text(manuscript)
 title={'108':'连续对应与最优化稳定性','109':'向量、凸性与无穷远方向'}[lec]
 cover=r'''\input{preamble.tex}
\newcommand{\LectureID}{'''+lec+r'''}
\hypersetup{pdftitle={Lecture '''+lec+'：'+title+r'''},pdfauthor={中文自学讲义}}
\begin{document}
\begin{titlepage}
\vspace*{1.4cm}
{\Huge\sffamily 数理分析方法\par}
\vspace{.8cm}{\LARGE\sffamily '''+title+r'''\par}
\vspace{.5cm}{\Large Lecture '''+lec+r''' · 证明考试自学讲义\par}
\vspace{1cm}
按教师内容重新编写\quad 完整定义与命题\quad 分步证明与批注\par
\vspace{.7cm}
\textbf{给读者的话}\par
这份讲义从基本符号和证明动作讲起，按老师的顺序解释每组内容。每个证明写出条件、目标、构造与极限依据；跨页的论证连起来讲。正文不使用原课件截图，不要求对照另一份文件才能补完推导。\par
\textbf{范围与页码}\par
对应教师原课件 '''+lec+'-ZSM-PPT.pdf 的第 1--'+str(total)+r''' 页。章节标题标注原页范围，证明单独标注来源，末尾逐页索引可定位全部原页。\par
\textbf{内容标识}\par
“补充”用于补足基础或教师未展开的证明；“纠正”说明原稿的笔误、条件缺失或无效推导。本讲义是自学辅助材料，不代表教师官方讲义。\par
\vfill
编写日期：2026 年 10 月 27 日\par
参考背景：Gérard Debreu, \emph{Theory of Value}，第1章相关内容。
\end{titlepage}
\tableofcontents\clearpage
\input{foundations.tex}
\input{body-'''+lec+r'''.tex}
\end{document}
'''
 (OUT/f'gpt-{lec}-exam.tex').write_text(cover)
 manifest[lec]={'page_map':{str(p):{'section_start':a,'section_title':t} for a,b,t in CFG['GROUPS'][lec] for p in range(a,b+1)},'source_pages':total,'all_pages_mapped':True,'teacher_proof_units':len(entries),'rendered_proof_sections':len(rendered),'proofs':rendered,'source_sha256':hashlib.sha256((ROOT/f'sources/{lec}-ZSM-PPT.pdf').read_bytes()).hexdigest()}
(HERE/'coverage.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({k:{x:v[x] for x in ['source_pages','teacher_proof_units','rendered_proof_sections']} for k,v in manifest.items()},ensure_ascii=False))

combined = r"""\input{preamble.tex}
\newcommand{\LectureID}{108、109}
\renewcommand{\contentsname}{108与109总目录}
\hypersetup{pdftitle={108与109：证明考试自学讲义}}
\begin{document}
\begin{titlepage}
\vspace*{2cm}{\Huge 数理分析方法\par}
\vspace{1cm}{\LARGE 108与109：证明考试自学讲义\par}
\vspace{1cm}连续对应与最优化稳定性\par 向量、凸性与无穷远方向\par
\vfill 本合订版使用统一总目录及连续页码。点击目录可跳转到两讲各节。\par
目录修订：2026年10月28日
\end{titlepage}
\setcounter{page}{2}
\tableofcontents
\clearpage
\renewcommand{\LectureID}{108}
\renewcommand{\theHsection}{108.\arabic{section}}
\part{Lecture 108：连续对应与最优化稳定性}
\input{foundations.tex}
\input{body-108.tex}
\clearpage
\renewcommand{\LectureID}{109}
\setcounter{section}{0}
\renewcommand{\theHsection}{109.\arabic{section}}
\part{Lecture 109：向量、凸性与无穷远方向}
\input{foundations.tex}
\input{body-109.tex}
\end{document}
"""
(OUT/'gpt-108-109-exam.tex').write_text(combined)
