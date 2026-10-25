from pathlib import Path
import json
E=json.loads((Path(__file__).resolve().parents[1]/'enhancements.json').read_text())
BLOCKS={k:v for k,v in E.items() if k.startswith(('102:','103:','104:'))}
BLOCKS['102:40']=r'''
\paragraph{第一题：含有“对任意集合”的等式}
假设 $\forall E\subseteq S,E\cap A=E\cup A'$。这个量词允许我们选择特别方便的 $E$，但结论必须来自所选等式本身。
先令 $E=S$：左边 $S\cap A=A$，右边 $S\cup A'=S$，所以 $A=S$。再照老师令 $E=CA=S\setminus A$，则 $E\cap A=\varnothing$，已知等式给 $\varnothing=CA\cup A'$。并集为空意味着两个集合都空，尤其 $A'=\varnothing$。这里即使不先代入 $A=S$，也能从 $A'\subseteq\varnothing$ 得结论。
\paragraph{第二题：与同一集合交、并相同能否认定相等}
必要性：若 $A_1=A_2$，取任意 $A_3$（例如空集），两个交及两个并当然分别相同。
充分性：设 $A_1\cap A_3=A_2\cap A_3$ 且 $A_1\cup A_3=A_2\cup A_3$。对任意 $i=1,2$，由 $A_3\cup CA_3=S$ 和分配律，
\[A_i=A_i\cap S=A_i\cap(A_3\cup CA_3)=(A_i\cap A_3)\cup(A_i\cap CA_3).\]
第一部分已由交集假设相等。要比较第二部分，对并集等式两边都交 $CA_3$：
\begin{align*}
(A_1\cup A_3)\cap CA_3&=(A_1\cap CA_3)\cup(A_3\cap CA_3)=A_1\cap CA_3,\\
(A_2\cup A_3)\cap CA_3&=A_2\cap CA_3.
\end{align*}
故外部两部分也相等，再代回拆分式便得 $A_1=A_2$。原页把拆分的首式写成与空集取并再分配，缺了 $A_i\cap(A_3\cup CA_3)$ 这个正确中间式；上面的写法修正这一点，保留老师的“分内外两块”路线。
'''
BLOCKS['102:42']=r'''
所有补集相对于同一全集 $S$。先化简老师给的表达式：
\begin{align*}
C(E\cap A)\cap(CE\cup A)
&=(CE\cup CA)\cap(CE\cup A)&&\text{德摩根律}\\
&=CE\cup(CA\cap A)&&\text{分配律的逆向}\\
&=CE\cup\varnothing=CE.&&\text{互补及空集恒等律}
\end{align*}
因此原方程恰好等价于 $A'=CE$。两边取补便等价于 $CA'=C(CE)=E$，这已给出完整等价链。下面也按老师分别展开两方向。
若 $CA'=E$，则 $CE=A'$，代入第一步化简后的表达式即得 $C(E\cap A)\cap(CE\cup A)=A'$。
反向若原方程成立，对它取补：
\begin{align*}
CA'&=C\big(C(E\cap A)\cap(CE\cup A)\big)\\
&=C(C(E\cap A))\cup C(CE\cup A)&&\text{外层交的补变为并}\\
&=(E\cap A)\cup(E\cap CA)&&\text{双重补与德摩根律}\\
&=E\cap(A\cup CA)=E\cap S=E.&&\text{提取公共交因子}
\end{align*}
每个等号都是集合恒等式，不需要假设 $A'$ 是 $A$ 的补集；撇号只是另一个集合的名字。原文 $CA\cap\cup A$ 中多出的并号为笔误。
'''
BLOCKS['102:43']=r'''
\paragraph{第4(1)题：先把老师省掉的反向包含补齐}
已知 $A\cup A'=E\cup E'$，$A\cap E'=\varnothing$，$A'\cap E=\varnothing$。用共同并集插入老师的分配步骤：
\begin{align*}
A&=A\cap(A\cup A')=A\cap(E\cup E')\\
&=(A\cap E)\cup(A\cap E')=(A\cap E)\cup\varnothing=A\cap E.
\end{align*}
因为 $A=A\cap E\subseteq E$，得到 $A\subseteq E$。但这还不能推出相等。必须再计算
\begin{align*}
E&=E\cap(E\cup E')=E\cap(A\cup A')\\
&=(E\cap A)\cup(E\cap A')=(E\cap A)\cup\varnothing=E\cap A,
\end{align*}
故 $E\subseteq A$，两包含合成 $A=E$。
对另一对集合也要分别检查：
\[A'=A'\cap(E\cup E')=(A'\cap E)\cup(A'\cap E')=A'\cap E'\subseteq E',\]
\[E'=E'\cap(A\cup A')=(E'\cap A)\cup(E'\cap A')=E'\cap A'\subseteq A'.\]
这里 $E'\cap A=\varnothing$ 就是题设 $A\cap E'=\varnothing$。故 $A'=E'$。老师只写正向包含后宣布相等，这正是需要补足的逻辑缺口；共同并集相同本身不能消掉这个缺口。
\paragraph{第4(2)题：两个切片合回原集合}
此小题只需 $A\cup A'=E\cup E'$。令 $A_1=A\cap E,A_2=A\cap E'$，则
\begin{align*}
A_1\cup A_2&=(A\cap E)\cup(A\cap E')\\
&=A\cap(E\cup E')&&\text{分配律}\\
&=A\cap(A\cup A')&&\text{题设共同并集}\\
&=A.&&\text{吸收律}
\end{align*}
没有使用第(1)题的交为空条件，所以不要把两个小题的假设混用。
'''
BLOCKS['103:18']=r'''
先固定约定：$A\subseteq S$，$\Phi(A)=\bigcup_{x\in A}\Phi(x)$；输出的补集相对于\emph{实际值域} $T=\Phi(S)$，输入的补集相对于 $S$。对应单射指 $x\ne x'$ 时 $\Phi(x)\cap\Phi(x')=\varnothing$，不等于单值。
\paragraph{先证 $T\setminus\Phi(A)\subseteq\Phi(S\setminus A)$}
任取 $y\in T\setminus\Phi(A)$。由于 $y\in T=\Phi(S)$，存在至少一个 $x\in S$ 使 $y\in\Phi(x)$。如果这个 $x\in A$，则由集合像的定义有 $y\in\Phi(A)$，与选点矛盾。所以该见证 $x\notin A$，即 $x\in S\setminus A$。于是 $y\in\Phi(x)\subseteq\Phi(S\setminus A)$。任意 $y$ 都如此，完成此方向。
\paragraph{有单射条件时证明反向}
任取 $y\in\Phi(S\setminus A)$，由定义选 $x\in S\setminus A$ 且 $y\in\Phi(x)$。若 $y$ 还属于 $\Phi(A)$，便存在 $x'\in A$ 使 $y\in\Phi(x')$。因为 $x\notin A,x'\in A$，有 $x\ne x'$，但 $y\in\Phi(x)\cap\Phi(x')$，违反单射。故 $y\notin\Phi(A)$。又它在 $\Phi(S)=T$ 中，故 $y\in T\setminus\Phi(A)$。合并两方向得等号。
若陪域另含永远达不到的点 $y$，该点在左边补集中却没有任何原像，第一方向的选点就会失败；因此实际值域约定是证明真正用到的条件。
'''
BLOCKS['103:25']=r'''
设 $\Delta(x)=C$ 为常对应。老师要把固定集合 $C$ 从并集内部提出。先设 $A\ne\varnothing$，则 $\Delta(A)=\bigcup_{x\in A}C=C$。
\begin{align*}
(\Delta\cap\Phi)(A)
&=\bigcup_{x\in A}(\Delta\cap\Phi)(x)&&\text{集合的对应像定义}\\
&=\bigcup_{x\in A}(C\cap\Phi(x))&&\text{逐点交与常值定义}\\
&=C\cap\bigcup_{x\in A}\Phi(x)&&\text{交对任意并分配}\\
&=C\cap\Phi(A)=\Delta(A)\cap\Phi(A).
\end{align*}
第三行若仍感到跳步，逐元素核查：$y$ 在前一行当且仅存在 $x\in A$ 使 $y\in C$ 且 $y\in\Phi(x)$；因为条件 $y\in C$ 不依赖 $x$，这等价于 $y\in C$ 且存在 $x\in A$ 使 $y\in\Phi(x)$，正是后一行。
若 $A=\varnothing$，按集合像定义 $(\Delta\cap\Phi)(A)=\varnothing$，且 $\Delta(A)=\Phi(A)=\varnothing$，右边也为空。不能在空 $A$ 时继续使用 $\Delta(A)=C$，故空集情况必须独立处理。
'''
BLOCKS['103:29']=r'''
定义逆对应 $\Phi^-(y)=\{x\in S:y\in\Phi(x)\}$。先证明逐点的逆两次公式：任取 $x\in S,y\in T$，
\[y\in(\Phi^-)^-(x)\iff x\in\Phi^-(y)\iff y\in\Phi(x).\]
首个等价把第二次逆的定义展开，第二个等价展开第一次逆。故两个对应在每个输入 $x$ 的输出元素完全相同，即 $(\Phi^-)^-=\Phi$。
老师还把该结论写为集合像的形式。任取 $A\subseteq S$，
\begin{align*}
(\Phi^-)^-(A)
&=\{y\in T:\Phi^-(y)\cap A\ne\varnothing\}\\
&=\{y\in T:\exists x\in A,\ x\in\Phi^-(y)\}\\
&=\{y\in T:\exists x\in A,\ y\in\Phi(x)\}\\
&=\bigcup_{x\in A}\Phi(x)=\Phi(A).
\end{align*}
中间的见证 $x$ 必须属于 $A$，不能只属于 $S$。若 $A=\varnothing$，所有存在条件都假，两边同时为空，公式仍成立。逆对应不是必须存在的单值反函数；该结论适用于普通多值对应。
'''
BLOCKS['103:31']=r'''
设值均非空；若原对应允许空值，则先将输入限制在 $S^*=\{x:\Phi(x)\ne\varnothing\}$，以下输入补集均相对此域。定义 $\Phi^+(B)=\{x:\Phi(x)\subseteq B\}$，$\Phi^-(B)=\{x:\Phi(x)\cap B\ne\varnothing\}$。
\paragraph{两条补集对偶，逐行写出否定}
\begin{align*}
x\notin\Phi^+(B)&\iff\neg[\forall y\in\Phi(x),y\in B]\\
&\iff\exists y\in\Phi(x),y\notin B\\
&\iff\Phi(x)\cap(T\setminus B)\ne\varnothing\\
&\iff x\in\Phi^-(T\setminus B).
\end{align*}
所以 $S^*\setminus\Phi^+(B)=\Phi^-(T\setminus B)$。另一条：
\begin{align*}
x\notin\Phi^-(B)&\iff\neg[\exists y\in\Phi(x),y\in B]\\
&\iff\forall y\in\Phi(x),y\notin B\\
&\iff\Phi(x)\subseteq T\setminus B\\
&\iff x\in\Phi^+(T\setminus B).
\end{align*}
\paragraph{上逆像对并的包含}
若 $x\in\Phi^+(B_1)\cup\Phi^+(B_2)$，则所有输出都在 $B_1$ 中，或者所有输出都在 $B_2$ 中。任一情况都使所有输出在 $B_1\cup B_2$ 中，所以 $x\in\Phi^+(B_1\cup B_2)$。反向不保证：值 $\{0,1\}$ 全在 $\{0\}\cup\{1\}$ 中，却不整体在任何单独一边。
\paragraph{下逆像对并的等式}
\begin{align*}
x\in\Phi^-(B_1\cup B_2)
&\iff\exists y\in\Phi(x),\ (y\in B_1\text{ 或 }y\in B_2)\\
&\iff[\exists y\in\Phi(x),y\in B_1]\text{ 或 }[\exists y\in\Phi(x),y\in B_2]\\
&\iff x\in\Phi^-(B_1)\cup\Phi^-(B_2).
\end{align*}
这四段完整对应老师两页的每条公式。上下逆像的差别就是“全部”与“至少一个”，所以并集公式不能互换。
'''
BLOCKS['103:35']=r'''
设 $f:A\to\mathcal P(A)$ 为任意函数。要证它不是满射，必须构造一个 $A$ 的子集不等于任何 $f(a)$。老师构造
\[B=\{a\in A:a\notin f(a)\}.\]
首先 $B\subseteq A$，故确实是陪域 $\mathcal P(A)$ 中的合法对象。反设存在 $b\in A$ 满足 $f(b)=B$。对该点只有两种可能：
\begin{enumerate}
\item 若 $b\in B$，按 $B$ 的定义有 $b\notin f(b)$；代入 $f(b)=B$ 得 $b\notin B$，矛盾。
\item 若 $b\notin B$，因为 $b\in A$，按 $B$ 的定义取否定有 $b\in f(b)$；代入得 $b\in B$，也矛盾。
\end{enumerate}
两种情形都不可能，所以没有 $b$ 使 $f(b)=B$。$f$ 任意，任何函数都不能满射到幂集。
取 $A=\N$，若其幂集可数，便能按正整数列出所有子集，也就是存在满射 $f:\N\to\mathcal P(\N)$，与上面结论矛盾。因此幂集不可数。对角集合不是随便挑的：它在第 $a$ 个位置专门与第 $a$ 个被列出的集合反着选，从而同时避开整个列表。
'''
BLOCKS['104:17']=r'''
负传递定义是：对所有 $x,y,z$，$\neg(xRy)$ 且 $\neg(yRz)$ 推出 $\neg(xRz)$。固定任意三点，把这个蕴含取逆否：
\begin{align*}
[\neg(xRy)\land\neg(yRz)]\Rightarrow\neg(xRz)
\quad\Longleftrightarrow\quad
xRz\Rightarrow\neg[\neg(xRy)\land\neg(yRz)].
\end{align*}
再由德摩根律和双重否定，右端的否定合取等价于 $(xRy)\lor(yRz)$。所以得到 $xRz\Rightarrow(xRy\text{ 或 }yRz)$。
反向从这一形式再次取逆否，便回到负传递，故不仅是单向推论。三点任意意味着中间点 $y$ 可以任意取；“或”允许两项都真，并不要求恰好一项真。
'''
BLOCKS['104:19']=r'''
严格偏好 $\succ$ 假定非对称且负传递。
\paragraph{非自反}若某点 $x\succ x$，对这一关系用非对称性又得 $\neg(x\succ x)$，矛盾，所以每个点都不严格优于自身。
\paragraph{传递}设 $x\succ y$ 且 $y\succ z$。由上条负传递的等价式，对关系 $x\succ y$ 插入中间点 $z$，得到 $x\succ z$ 或 $z\succ y$。后一分支与题设 $y\succ z$ 的非对称性矛盾，所以只能 $x\succ z$。这就是普通传递。
\paragraph{无循环}若存在有限循环 $x_1\succ x_2\succ\cdots\succ x_m\succ x_1$，重复使用刚证的传递性，先得 $x_1\succ x_3$，再得 $x_1\succ x_4$，最终得 $x_1\succ x_m$。再与最后一条 $x_m\succ x_1$ 传递，得到 $x_1\succ x_1$，与非自反矛盾。因此任何有限长度的严格循环都不存在。
三个性质不能直接互相混称：非对称排除两点反向，非自反排除单点循环，完整的无循环性还用到了传递。
'''
BLOCKS['104:28']=r'''
给定完全传递的 $\succeq'$，定义 $x\succ' y\iff\neg(y\succeq' x)$，并定义 $x\sim' y\iff x\succeq' y$ 且 $y\succeq' x$。原页无差异定义第二项写成 $y\succeq' y$ 是笔误，必须先修正。
\paragraph{非对称}若 $x\succ' y$，则 $\neg(y\succeq' x)$。完全性迫使 $x\succeq' y$ 成立。若又 $y\succ' x$，按定义就是 $\neg(x\succeq' y)$，矛盾。所以 $\succ'$ 非对称。
\paragraph{负传递}设 $\neg(x\succ' y)$ 且 $\neg(y\succ' z)$。展开定义并消去双重否定，得到 $y\succeq' x,z\succeq' y$。原弱关系传递给 $z\succeq' x$，其等价写法正是 $\neg(x\succ' z)$。因此新严格关系负传递。
\paragraph{还原弱关系}从新严格关系再定义 $x\succeq y\iff\neg(y\succ' x)$。逐层代入得
\[x\succeq y\iff\neg[\neg(x\succeq' y)]\iff x\succeq' y.\]
这同时证明两个包含方向，不需要把完全性再使用一次。
\paragraph{还原无差异}新无差异为 $x\sim y\iff\neg(x\succ' y)\land\neg(y\succ' x)$。代入定义得 $y\succeq' x$ 且 $x\succeq' y$，交换两个合取条件就是 $x\sim' y$。因此两种从严格或弱关系出发的构造真正互相还原。
'''
BLOCKS['102:33']=r'''
令 $A=A_1,B=A_2,C=A_3$。老师的路线是\emph{两边分别展开，化成相同四项}。定义 $X\triangle Y=(X\setminus Y)\cup(Y\setminus X)$，以及等价式 $(X\cup Y)\setminus(X\cap Y)$。
\paragraph{先展开左括号版本}
\begin{align*}
(A\triangle B)\triangle C
&=\{[(A\setminus B)\cup(B\setminus A)]\setminus C\}
 \cup\{C\setminus[(A\cup B)\setminus(A\cap B)]\}\\
&=[(A\setminus B)\setminus C]\cup[(B\setminus A)\setminus C]\\
&\qquad\cup\{C\cap[(A\cup B)^c\cup(A\cap B)]\}\\
&=[A\cap (B\cup C)^c]\cup[B\cap (A\cup C)^c]\\
&\qquad\cup[C\cap (A\cup B)^c]\cup(A\cap B\cap C)\\
&=[A\setminus(B\cup C)]\cup[B\setminus(A\cup C)]\\
&\qquad\cup[C\setminus(A\cup B)]\cup(A\cap B\cap C).
\end{align*}
这里补集统一用上标 $c$ 表示，与第三集合 $C$ 区分。
第二个等号对第一大括号使用并的差分配，对第二大括号使用
\[(X\setminus Y)^c=C(X\cap Y^c)=X^c\cup Y.\]
第三个等号用 $(A\setminus B)\setminus C=A\cap B^c\cap C^c=A\cap (B\cup C)^c$，其他项同理；再将交对并分配。每条等式均来自已知集合律，没有引用本条待证的对称差结合律。
\paragraph{再展开右括号版本，不能省成“同理”}
\begin{align*}
A\triangle(B\triangle C)
&=\{A\setminus[(B\cup C)\setminus(B\cap C)]\}\\
&\qquad\cup\{[(B\setminus C)\cup(C\setminus B)]\setminus A\}\\
&=\{A\cap[(B\cup C)^c\cup(B\cap C)]\}\\
&\qquad\cup[(B\setminus C)\setminus A]\cup[(C\setminus B)\setminus A]\\
&=[A\setminus(B\cup C)]\cup(A\cap B\cap C)\\
&\qquad\cup[B\setminus(A\cup C)]\cup[C\setminus(A\cup B)].
\end{align*}
最后只需用\emph{并集}的交换、结合律调换这四项顺序，便与第一段最终表达式相同。故 $(A\triangle B)\triangle C=A\triangle(B\triangle C)$。
原页右侧展开中有一项把 $C\cap (A\cup B)^c$ 误写为与交集相交，须按这里的第三个“只属于一边”项修正；否则无法得到下一行。此处也显示三者共有部分属于三重对称差，而不是被删除。
'''
BLOCKS['102:36']=r'''
按原页把左右两边都化成 $[A\cap(B\cup C)]\setminus(A\cap B\cap C)$。先令 $T=A\cap B\cap C$，避免长公式掩盖步骤。
\paragraph{老师第一串等号}
\begin{align*}
A\cap(B\triangle C)
&=A\cap[(B\setminus C)\cup(C\setminus B)]&&\text{对称差定义}\\
&=[A\cap(B\setminus C)]\cup[A\cap(C\setminus B)]&&\text{交对并分配}\\
&=\{A\cap[B\setminus(B\cap C)]\}\cup\{A\cap[C\setminus(B\cap C)]\}\\
&=[(A\cap B)\setminus T]\cup[(A\cap C)\setminus T]\\
&=[(A\cap B)\cup(A\cap C)]\setminus T\\
&=[A\cap(B\cup C)]\setminus T.
\end{align*}
第三行因为在 $B$ 内排除 $C$ 与排除 $B\cap C$ 相同，在 $C$ 内也同理。第四行把固定集合 $A$ 交进去后，被删掉的共同部分正是 $T$。第五行是两个集合同时减去同一 $T$ 可先并再减；逐元素都是“属于至少一边且不在 $T$”。第六行再次使用分配律。
\paragraph{老师第二串等号}
\begin{align*}
(A\cap B)\triangle(A\cap C)
&=[(A\cap B)\setminus(A\cap C)]\cup[(A\cap C)\setminus(A\cap B)]\\
&=[(A\cap B)\setminus T]\cup[(A\cap C)\setminus T]\\
&=[(A\cap B)\cup(A\cap C)]\setminus T\\
&=[A\cap(B\cup C)]\setminus T.
\end{align*}
第二个等号的理由是：对本已在 $A\cap B$ 的点，是否还在 $A\cap C$ 等价于是否在三重交 $T$；另一边对称。两串等号最后得到同一个集合，所以目标等式成立。这一版完整保留了老师经“三重共同部分”的推导，没有用另一条更短的补集计算替代。
'''
# Expand the second branch explicitly rather than directing a beginner to repeat it mentally.
BLOCKS['104:22']=BLOCKS['104:22'].replace('对 $y\\sim z,z\\succ w$ 同理得 $y\\succ w$。',r'''第二种连接设 $y\sim z,z\succ w$。对 $y,w$ 的三分性，若 $w\succ y$，传递性与 $z\succ w$ 给 $z\succ y$，违反 $y\sim z$；若 $w\sim y$，再与 $y\sim z$ 传递得 $w\sim z$，违反 $z\succ w$。所以只能 $y\succ w$。将两种连接用于 $x\succ y,y\sim z,z\succ w$，便分别得到 $x\succ z$、$y\succ w$，再用严格传递还可得 $x\succ w$。''')
BLOCKS['102:33']=BLOCKS['102:33'].replace(r'C(X\cap Y^c)',r'(X\cap Y^c)^c')
