from pathlib import Path
import re,json,fitz
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'proofs'
# Each entry lists actual source proof pages, grouped along the lecturer's derivation.
entries={
'000-ZSM':[(19,20),(21,22),(24,24),(25,25),(28,28),(29,29),(31,31),(32,32),(33,33),(34,34),(35,35),(36,37),(39,40),(41,42),(43,44),(46,47)],
'102':[(33,33),(34,34),(36,36),(37,37),(38,38),(40,40),(42,42),(43,43)],
'103':[(18,18),(25,25),(28,28),(29,29),(31,32),(35,35)],
'104':[(17,17),(19,19),(22,22),(28,28)],
'105':[(37,38),(39,40),(42,42),(43,43),(46,46),(47,47),(49,49),(50,50),(51,51),(52,52),(53,53),(54,55),(57,58),(59,60),(61,62),(64,65)],
'106':[(8,8),(18,18),(19,19),(20,20),(22,23),(24,25),(26,27),(28,28),(30,30),(31,31),(33,33),(34,34),(35,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(46,46),(47,47),(48,48),(49,49),(50,50),(51,51),(52,52),(54,54),(55,56),(57,57),(60,60),(61,63),(64,64),(65,65),(66,66),(70,71),(72,72),(73,73),(74,74),(75,75),(79,79),(80,80),(81,81),(84,85),(92,92),(94,94),(96,96),(98,99)],
'107':[(9,11),(13,13),(14,14),(15,15),(16,16),(18,18),(19,19),(26,26),(27,27),(28,28),(29,29),(30,30),(31,32),(33,33),(34,35),(36,36),(37,37),(38,38),(39,39),(40,40),(41,41),(42,42),(43,43)],
'108':[(11,11),(12,12),(14,14),(19,19),(20,20),(21,21),(29,30),(32,33),(34,34),(39,39),(40,40),(41,41),(42,42),(43,43),(44,44),(45,45),(47,49),(51,51),(52,53),(55,55),(56,56),(57,57),(58,58),(59,59),(60,60),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),(70,70),(71,72),(73,74),(75,76),(78,79),(80,80),(81,81),(82,82),(83,83),(85,86),(87,89),(90,90),(91,91),(92,92),(93,93),(94,94),(95,95),(96,96),(98,98),(99,99),(101,101),(102,102),(103,104),(105,106),(107,107),(110,111),(113,113)],
'109':[(10,10),(11,11),(12,12),(13,13),(17,17),(23,23),(25,25),(29,29),(30,30),(31,31),(32,32),(33,33),(35,35),(36,36),(38,41),(43,44),(45,45),(49,49),(50,50),(51,51),(52,52),(53,53),(54,54),(57,59),(69,70),(77,78),(79,79),(80,80),(82,82),(83,83),(84,84),(85,85),(86,86),(87,87),(88,88),(89,89),(90,90),(91,91),(93,96),(98,100),(101,103),(106,107),(108,108),(110,111),(112,112),(113,113),(114,114),(115,115),(117,118)],
'110':[(5,5),(6,6)]}
# Notes text is reused only as commentary, never as evidence of a proof in the source.
notes={};titles={};loc={}
for key in entries:
 s=(ROOT/'notes'/f'{key}-body.tex').read_text(); parts=re.split(r'\\Slide\{(\d+)\}\{([^\n]*)\}\n',s)
 notes[key]={};titles[key]={}
 # split with three captures? actually two captures -> groups of 3
 notes[key]={};titles[key]={}
 for i in range(1,len(parts),3):
  n=int(parts[i]);titles[key][n]=parts[i+1];body=parts[i+2]
  body=body.split('\\clearpage\\section*')[0].strip()
  notes[key][n]=body
 for n,body in list(notes[key].items()):
  m=re.search(r'完整定义、条件和论证见本讲原页第 (\d+) 页下方',body)
  if m:notes[key][n]=notes[key][int(m.group(1))]
 # physical PDF pages and printed footer corresponding to each original slide
 loc[key]={}
 for i,pg in enumerate(fitz.open(ROOT/'pdf'/f'gpt-{key}.pdf')):
  t=pg.get_text();m=re.search(r'原课件第\s*(\d+)\s*页',t)
  if m:loc[key][int(m.group(1))]=(i+1,t.strip().splitlines()[-1])
# optional hand-written enhancements replacing overly compressed commentary
statements=json.loads((out/'statements.json').read_text())
extra=json.loads((out/'enhancements.json').read_text()) if (out/'enhancements.json').exists() else {}
tex=[r'''\input{tex/preamble.tex}
\newcommand{\LectureID}{Proof 汇编}
\makeatletter
\renewcommand{\l@subsection}{\@dottedtocline{2}{1.5em}{3.8em}}
\makeatother
\begin{document}
\begin{titlepage}\vspace*{2cm}{\Huge 数理分析方法\par}\vspace{1cm}{\LARGE 证明详解：按老师课件路线重写\par}\vspace{1cm}中文命题 · 证明思路 · 逐步推导 · 来源页码\par\vfill
\textbf{收录边界}\par
仅以 sources/ 中老师原始课件是否实际展示论证为依据。收录显式 Proof、跨页续证、公式推导及带理由的例证；不因出现 “One can prove” 或 Questions/Prove 就收录。只陈述定理而没有推导的不补入。相同证明在不同课件重复出现时保留各自来源。
\textbf{阅读约定}\par
每项以重新排版的文字和数学公式写出命题、证明思路与推导，不嵌入任何课件原页或截图。来源页码只用于核对。补充与纠错单独标明，不假称为教师原文。伪证明保留作辨错，明确不作为有效证明。原课件PDF页码从封面计1；另列已有 gpt 讲义对应页脚，避免把两套页码混淆。证明跨页时统一列出范围。
\textbf{重要说明}\par
教师出现了不完整论证时，依其原路线补足；原命题不成立时，说明具体错误，不把它包装为正确证明。108的伪定理条目属于原课件实际展示的错误论证。高维 Brouwer、Kakutani 仅陈述，故其证明不在本汇编。
2026 年 10 月 25 日\end{titlepage}
\tableofcontents\clearpage
\section{000-Intro-Proof：无实际证明过程}
000-PPT.pdf 为课程概览和人物介绍，没有符合本汇编范围的证明，因此不添加任何证明。
''']
manifest=[]
for key,spans in entries.items():
 if key=='102':tex.append(r'\clearpage\section{101-Proof：无实际证明过程}101-ZSM-PPT.pdf 为数学章节引言，没有实际证明过程，故不添加证明。')
 label='000-Proof（000-ZSM）' if key=='000-ZSM' else key+'-Proof'
 tex.append('\\clearpage\\section{'+label+'}')
 source=key+'-PPT.pdf' if key=='000-ZSM' else key+'-ZSM-PPT.pdf'
 for idx,(a,b) in enumerate(spans,1):
  title=titles[key][a];pages=str(a) if a==b else f'{a}--{b}'
  tex.append('\\clearpage\\subsection{'+title+'}')
  tex.append(f'\\textbf{{来源：}}\\texttt{{{source}}}，原课件 PDF 第 {pages} 页。\\par')
  refs=[]
  for n in range(a,b+1):
   if n in loc[key]:refs.append(loc[key][n][1])
  if refs:tex.append(f'对应已有 \\texttt{{gpt-{key}.pdf}} 页脚：'+', '.join(refs)+'。\\par')
  spec=statements[key+':'+str(a)]
  tex.append('\\paragraph{命题与条件}'+spec['statement'])
  tex.append('\\paragraph{证明思路}'+spec['idea'])
  tex.append('\\paragraph{详细推导与必要批注}')
  bodies=[]
  for n in range(a,b+1):
   body=notes[key][n]
   if body not in bodies:bodies.append(body)
  custom=extra.get(key+':'+str(a))
  body=custom if custom else '\n\n'.join(bodies)
  body=body.replace('原图','原课件').replace('本页','原课件该页').replace('截图','原课件')
  tex.append(body)
  manifest.append(dict(lecture=key,item=idx,source=source,proof_pages=list(range(a,b+1)),title=title,note_footers=refs))
tex.append(r'\end{document}')
(out/'all-proofs.tex').write_text('\n'.join(tex))
(out/'proof-index.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('entries',len(manifest),'pages',sum(len(x['proof_pages']) for x in manifest))
