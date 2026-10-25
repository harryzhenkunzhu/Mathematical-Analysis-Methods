BLOCKS={}
def put(n,s):BLOCKS[f'106:{n}']=s
put(8,r'''
令 $a_i=|x_i-y_i|$，$M=\max_{1\le i\le N}a_i$。目标为 $\lim_{p\to\infty}(\sum_i a_i^p)^{1/p}=M$。老师原页以对数和极限式化简，但当某 $a_i=0$ 时 $\log a_i$ 未定义，且交换极限与加权和需要理由。下面保留“最大坐标主导”的思路，把遗漏理由写成可逐步核验的估计。
若 $M=0$，所有坐标差均0，每个 $p$ 的范数都0，结论成立。若 $M>0$，至少有一个 $a_j=M$，且每个 $a_i\le M$，故
\[M^p\le\sum_{i=1}^N a_i^p\le NM^p.\]
三者非负，取正的 $p$ 次方根保持顺序：
\[M\le\left(\sum_i a_i^p\right)^{1/p}\le N^{1/p}M.\]
因为 $N$ 是固定有限整数，$N^{1/p}=\exp((\log N)/p)\to1$。上下界同时趋于 $M$，夹逼给所需极限。这样也严格解释老师为什么最后只剩最大坐标，而无需给0取对数。
''')
put(18,r'''
\paragraph{收敛互异点列推出聚点}设 $x_n\in E$ 互不相同且 $x_n\to x$。任给球 $B(x,r)$，收敛性给 $N$，使所有 $n\ge N$ 的点都在球内。这是无穷多个不同点，而不是同一点重复无穷次，所以球含无穷多个 $E$ 元素，$x\in E'$。
\paragraph{聚点推出互异收敛点列}设每个 $B(x,r)$ 都含无穷多个 $E$ 元素。从 $B(x,1)\cap E$ 选 $x_1\ne x$。已选 $x_1,\ldots,x_n$ 后，$B(x,1/(n+1))\cap E$ 无限，删去有限集 $\{x,x_1,\ldots,x_n\}$ 仍非空，选其一点为 $x_{n+1}$。
于是所有点属于 $E$、互异，且 $\|x_n-x\|<1/n$。给任意 $\eps>0$，选 $N>1/\eps$，则 $n\ge N$ 时 $1/n<\eps$，所以 $x_n\to x$。排除已选点的步骤是必要的，否则常值列只能证明闭包归属，不能证明聚点。
''')
put(19,r'''
先核查老师引用的单调性：若 $A\subseteq B$ 且 $x\in A'$，则每个球中无穷多个 $A$ 元素也都在 $B$ 中，故 $x\in B'$。又 $\overline A=A\cup A'$，所以闭包也单调。
\paragraph{容易方向}因 $A,B\subseteq A\cup B$，单调性分别给 $A',B'\subseteq(A\cup B)'$，再取并得 $A'\cup B'\subseteq(A\cup B)'$。
\paragraph{反向}任取 $x\in(A\cup B)'$。若 $x\notin A'$ 且 $x\notin B'$，就分别存在正半径 $r_A,r_B$，使对应球内只有有限多个 $A$ 点、有限多个 $B$ 点。取 $r=\min(r_A,r_B)>0$，球 $B(x,r)$ 内的 $A\cup B$ 点是两个有限集合的并，因此仍有限，与 $x$ 为并集聚点矛盾。所以 $x$ 至少在 $A',B'$ 中一个，得到反向包含。
这里有限性非常关键；无限多个有限点集的并可以产生新聚点，所以不能将式子直接推广成无限并。
''')
put(20,r'''
先证内部单调：若 $A\subseteq B$ 且 $x\in A^\circ$，存在球 $B(x,r)\subseteq A\subseteq B$，故 $x\in B^\circ$。
因 $A\cap B\subseteq A,B$，单调性给 $(A\cap B)^\circ\subseteq A^\circ\cap B^\circ$。反过来，任取 $x\in A^\circ\cap B^\circ$，分别选 $r_A,r_B>0$ 使 $B(x,r_A)\subseteq A$ 和 $B(x,r_B)\subseteq B$。令 $r=\min(r_A,r_B)>0$，则任意 $y\in B(x,r)$ 同时在两个球内，所以 $y\in A\cap B$。故 $B(x,r)\subseteq A\cap B$，$x$ 为交集内点。
两个包含证明相等。注意半径属于同一个中心 $x$；不能仅说两个集合各自有某个球就得它们的交有球。
''')
put(22,r'''
设无限 $E\subseteq\R^N$ 有界，取一个包含它的闭立方体 $Q_0$，边长 $L>0$。把每边二分，得到 $2^N$ 个闭子立方体，至少一个与 $E$ 的交无限；否则有限多个有限集合的并会使 $E$ 有限。保留这一块 $Q_1$。依次二分，得到嵌套 $Q_k$，边长 $L/2^k$，每块仍含无穷多个 $E$ 点。
每个坐标方向都是闭区间套，长度趋零，由实数区间套定理各有唯一交点坐标 $a_i$，故 $a=(a_1,\ldots,a_N)$ 同时在所有 $Q_k$ 中。在欧氏距离下块的直径为 $\sqrt N L/2^k\to0$；在最大范数下为 $L/2^k$，结论相同。
任给 $r>0$，选 $k$ 使直径小于 $r$。任意 $z\in Q_k$ 与 $a$ 同在该块，故 $\|z-a\|<r$，即 $Q_k\subseteq B(a,r)$。于是 $B(a,r)$ 含 $E\cap Q_k$ 的无穷多个元素。每个 $r$ 都成立，$a$ 为聚点。原课件从多维立方体缩回到一点的中间理由就是逐坐标应用区间套，不能省略。
''')
put(24,r'''
设每个 $P\in E$ 都孤立。依老师选 $\delta_P>0$ 使 $B(P,2\delta_P)\cap E=\{P\}$；若最初只有半径 $r_P$，取 $\delta_P=r_P/2$ 即可。由 $\Q^N$ 稠密，从 $B(P,\delta_P)$ 选一个有理坐标点 $R_P$。
要推出可数，关键必须证明映射 $P\mapsto R_P$ 单射。反设 $P_1\ne P_2$ 却 $R_{P_1}=R_{P_2}=R$。三角不等式给
\[\|P_1-P_2\|\le\|P_1-R\|+\|R-P_2\|<\delta_{P_1}+\delta_{P_2}\le2\max(\delta_{P_1},\delta_{P_2}).\]
若最大的是 $\delta_{P_1}$，则 $P_2\in B(P_1,2\delta_{P_1})\cap E$，但这个交应只含 $P_1$，矛盾。若最大的是 $\delta_{P_2}$，同理 $P_1$ 落进只允许 $P_2$ 的孤立球，也矛盾。因此映射单射。
$\Q^N$ 是有限个可数集的积，仍可数，故其子集 $\{R_P:P\in E\}$ 可数，单射使 $E$ 也至多可数。原页交集写成 $\{P_1,P_2\}$ 应理解为与先前单点条件矛盾，并非承认该交本来可有两个点。
''')
put(26,r'''
采用聚点定义：每个邻域含无穷多个不同 $E$ 点。必要性很直接：无限集合删掉中心 $P$ 这至多一点仍非空，故每个去心球遇到 $E$。
反向假设每个 $B(P,r)\setminus\{P\}$ 都遇到 $E$。要证每个球含无穷多个不同点。反设某个 $B(P,r_0)$ 内只有有限多个非中心点 $Q_1,\ldots,Q_m$。若 $m=0$，已直接违反假设。若 $m>0$，有限个正数 $\|Q_i-P\|$ 有正的最小值 $d$。取 $r=\min(r_0,d/2)>0$，则该小球内不可能含任何 $Q_i$，又在原大球内，不会出现列表之外的新点。删去中心后为空，违反假设。
所以每个邻域中非中心点必无限，$P\in E'$。这里“找一个点”与“有无穷多个点”的桥梁正是有限个正距离能取正最小值。
''')
put(28,r'''
若 $P$ 是内点，按定义已有 $r>0$ 使 $B(P,r)\subseteq E$。老师还要说明反向邻域条件确实使 $P$ 位于内部，并说明这个球内的其他点同样是内点。
设 $B(P,r)\subseteq E$。任取 $Q\in B(P,r)$，令 $s=r-\|Q-P\|>0$。若 $Z\in B(Q,s)$，三角不等式给
\[\|Z-P\|\le\|Z-Q\|+\|Q-P\|<s+\|Q-P\|=r.\]
所以 $B(Q,s)\subseteq B(P,r)\subseteq E$。尤其 $Q=P$ 时给出一个以 $P$ 为中心完全在 $E$ 内的球，正是内点条件；对任意 $Q$ 的论证进一步证明该球整体落在 $E^\circ$ 中。这解释后续内部为何开。
''')
put(30,r'''
设 $f:\R^N\to\R$。\textbf{正向：}若 $f$ 连续，固定任意 $t$，令 $F_+=\{x:f(x)\ge t\}$。对任意 $x_k\in F_+$ 且 $x_k\to x$，有 $f(x_k)\to f(x)$。因为每个 $f(x_k)\ge t$，极限也 $\ge t$（若极限更小，取差的一半作精度便矛盾）。故 $x\in F_+$，该集闭。对 $F_-=\{f\le t\}$，取任意 $x_k\in F_-$ 趋于 $x$，连续性给 $f(x_k)\to f(x)$，每项 $f(x_k)\le t$ 使极限也 $\le t$，故 $x\in F_-$，它也闭。
\textbf{反向：}假设所有这两类弱水平集都闭。固定 $x_0$ 和 $\eps>0$，取开集
\[G_1=\{x:f(x)>f(x_0)-\eps\}=\R^N\setminus\{f\le f(x_0)-\eps\},\]
\[G_2=\{x:f(x)<f(x_0)+\eps\}=\R^N\setminus\{f\ge f(x_0)+\eps\}.\]
两集开且都含 $x_0$。因此交中存在球 $B(x_0,\delta)$。其中每个 $x$ 满足 $f(x_0)-\eps<f(x)<f(x_0)+\eps$，等价于 $|f(x)-f(x_0)|<\eps$，这正是连续定义。每个阈值任意这一假设使我们能按当前 $x_0,\eps$ 选择这两个具体阈值。
''')
put(31,r'''
设 $r>0$，$U=B(x_0,r)$ 为开球，$F=\{x:\|x-x_0\|\le r\}$ 为闭球。先证 $F$ 闭：若 $z_n\in F,z_n\to z$，反三角不等式 $|\|z_n-x_0\|-\|z-x_0\||\le\|z_n-z\|$ 使距离趋于 $\|z-x_0\|$，故该极限仍不超过 $r$，$z\in F$。由于 $U\subseteq F$ 且 $F$ 闭，最小闭超集性质给 $\overline U\subseteq F$。
反向任取 $x\in F$。令 $x_k=x_0+(1-1/k)(x-x_0)$，其中 $k\ge1$。则
\[\|x_k-x_0\|=(1-1/k)\|x-x_0\|\le(1-1/k)r<r,\]
所以每个 $x_k\in U$。又 $x_k-x=-(x-x_0)/k\to0$，故 $x_k\to x$。闭包包含原集合中序列的一切极限，所以 $x\in\overline U$。于是 $F\subseteq\overline U$，合得等号。条件 $r>0$ 用在严格小于处；半径0的开球是空集，其闭包不是单点闭球。
''')
put(33,r'''
\paragraph{先证导集闭，即 $(E')'\subseteq E'$}
任取 $P\in(E')'$。固定任意半径 $r>0$，可从 $B(P,r/2)\cap E'$ 选 $Q\ne P$。令 $s=\min(r/2,\|Q-P\|/2)>0$。因 $Q\in E'$，球 $B(Q,s)$ 含无穷多个 $E$ 点；此球不含 $P$，而且由三角不等式包含于 $B(P,r)$。故 $P$ 的每个邻域都含无穷多个 $E$ 点，$P\in E'$。所以 $E'$ 含自己的聚点，是闭集。
\paragraph{再证闭包闭}
$\overline E=E\cup E'$。已证有限并导集公式，因此
\[(\overline E)'=(E\cup E')'=E'\cup(E')'\subseteq E'\subseteq\overline E.\]
故闭包也含自己的聚点，是闭集。这里第二段用到了第一段 $(E')'\subseteq E'$，不能在尚未证明时把它当成当然结论。
''')
for n,closure,arbitrary in [(34,False,False),(35,True,False),(36,False,True),(37,True,True),(38,False,True),(39,True,True)]:
 if not arbitrary:
  body=(r'''设 $F=\bigcup_{i=1}^mF_i$，每个 $F_i$ 闭。有限并导集公式给
\[F'=\left(\bigcup_{i=1}^mF_i\right)'=\bigcup_{i=1}^mF_i'\subseteq\bigcup_{i=1}^mF_i=F.\]
包含号逐因子来自 $F_i'\subseteq F_i$，即闭性。$F'\subseteq F$ 是“包含所有聚点”的闭集判据，所以 $F$ 闭。有限并导集公式本身须由每个点的有限邻域论证建立，不能对无限并使用。''' if not closure else r'''设 $F=\bigcup_{i=1}^mF_i$。老师将闭包写成集合与导集之并：
\begin{align*}
\overline F&=F\cup F'=\left(\bigcup_iF_i\right)\cup\left(\bigcup_iF_i'\right)\\
&=\bigcup_i(F_i\cup F_i')=\bigcup_i\overline{F_i}=\bigcup_iF_i=F.
\end{align*}
第二个等号用了有限并导集公式，第三个等号只重排有限并。倒数第二步用每个因子闭，故等于自身闭包。$\overline F=F$ 是闭集判据，完成证明。此版本与上一版本目标相同，但明确保留老师经闭包重组的全部步骤。''')
 else:
  sym=r'\overline F' if closure else r"F'";fs=r'\overline{F_\gamma}' if closure else r"F_\gamma'"
  body=rf'''设 $F=\bigcap_{{\gamma\in\Gamma}}F_\gamma$，每个因子闭。固定任意 $\gamma$，交集定义给 $F\subseteq F_\gamma$；由{('闭包' if closure else '导集')}单调性得 ${sym}\subseteq {fs}$；由因子闭性得 ${fs}\subseteq F_\gamma$。因此 ${sym}\subseteq F_\gamma$ 对\emph{{每一个}} $\gamma$ 都成立，故
\[{sym}\subseteq\bigcap_\gamma F_\gamma=F.\]
这正是闭集判据，所以 $F$ 闭。若用闭包，还可加上恒成立的 $F\subseteq\overline F$ 得相等。这里不用对无穷多个半径取最小值，也不要求指标集可数：每个固定因子分别成立的归属，直接合为交集归属。原课件可数版本取 $\Gamma=\N$ 即可；任意指标版本的逻辑相同。'''
 put(n,body)
put(40,r'''
老师以闭区间 $F_k=[1/(k+1),1/k]$ 说明无限闭并可能不闭。各端点都在区间内，所以每个 $F_k$ 闭。证明并恰为 $(0,1]$：每个区间显然在 $(0,1]$ 内；若 $0<x\le1$，可找整数 $k\ge1$ 使 $k\le1/x\le k+1$（边界整数任选相邻区间），取倒数后得 $1/(k+1)\le x\le1/k$，所以 $x$ 在某个 $F_k$。
并集中点 $x_k=1/k$ 趋于0，但0不在任何 $F_k$ 中。于是并集不包含自身点列的极限，不闭。结论否定的是“任意无限闭并仍闭”，不是说每个无限闭并都一定不闭。
''')
put(41,r'''
令 $\mathcal F=\{F:A\subseteq F,F\text{ 闭}\}$，$H=\bigcap_{F\in\mathcal F}F$。该族非空，因为整个空间是闭超集。任意闭交闭，故 $H$ 闭，且 $A\subseteq H$。
若 $x\in\overline A=A\cup A'$，则对每个 $F\in\mathcal F$，$A\subseteq F$ 给 $A'\subseteq F'\subseteq F$，而 $A\subseteq F$，所以 $x\in F$。故 $x\in H$，得到 $\overline A\subseteq H$。
反向，已经证明 $\overline A$ 闭且含 $A$，所以 $\overline A$ 本身就在交集族 $\mathcal F$ 中。一个交集总包含于其中每一成员，特别 $H\subseteq\overline A$。两包含合并即为所求。老师使用“最小闭超集”时，其严格含义就是这两个包含，不是未经证明的直觉。
''')
put(42,r'''
设非空有界闭集 $F_1\supseteq F_2\supseteq\cdots$。在每个 $F_n$ 中取一点 $x_n$。全部点都在有界 $F_1$ 中，由 Bolzano--Weierstrass 可取严格递增指标 $n_k$ 及 $x_{n_k}\to x$。
固定\emph{任意}一个 $m$。因为 $n_k\to\infty$，存在 $K$ 使 $k\ge K$ 时 $n_k\ge m$；嵌套给 $F_{n_k}\subseteq F_m$，所以这个子列的整个尾部都在 $F_m$ 中。删去有限项不改变极限，$F_m$ 闭便给 $x\in F_m$。
这个论证对每个 $m$ 都成立，故 $x\in\bigcap_mF_m$，交非空。注意不是每个 $x_n$ 都在每个 $F_m$ 中；必须先固定 $m$ 再只看足够晚的子列。这里有界性实际只需对 $F_1$ 成立，后续由嵌套自动继承。
''')
put(46,r'''
任取 $x\in E^\circ$，定义给 $r>0$ 使 $B(x,r)\subseteq E$。为证内部开，需要证明这个大球还完全在 $E^\circ$，不能只知道它在 $E$。
任取 $y\in B(x,r)$，设 $s=r-\|y-x\|>0$。若 $z\in B(y,s)$，则
\[\|z-x\|\le\|z-y\|+\|y-x\|<s+\|y-x\|=r.\]
所以 $B(y,s)\subseteq B(x,r)\subseteq E$。由内点定义 $y\in E^\circ$，$y$ 任意便得 $B(x,r)\subseteq E^\circ$。故每个 $x\in E^\circ$ 有一个仍留在内部的球，内部开。若内部为空，空集按定义也开，已覆盖全部情形。
''')
put(47,r'''
令 $G=\bigcap_{i=1}^mG_i$，各 $G_i$ 开。先确认老师用到的恒等式：$(\bigcap_{i=1}^mG_i)^\circ=\bigcap_{i=1}^mG_i^\circ$。正向由内部单调性；反向对交中一点，分别选有限个内球，取最小正半径，便有共同内球。因此这条内部公式已经有严格依据。
现在代入 $G_i^\circ=G_i$，逐行得到
\[G^\circ=\left(\bigcap_iG_i\right)^\circ=\bigcap_iG_i^\circ=\bigcap_iG_i=G.\]
一个集合等于自身内部当且仅每个点都是内点，即开集。故 $G$ 开。若 $G$ 为空也满足同一等式。无限交不能随意使用内部公式，因为无穷个正半径的下确界可能为0。
''')
put(48,r'''
这是相同结论的直接邻域证明。任取 $x\in G=\bigcap_{i=1}^mG_i$。由每个 $G_i$ 开，取 $r_i>0$ 满足 $B(x,r_i)\subseteq G_i$。令 $r=\min\{r_1,\ldots,r_m\}$，有限多个正数的最小值仍正。
对任意 $y\in B(x,r)$，每个 $i$ 都有 $\|y-x\|<r\le r_i$，所以 $y\in G_i$。因此 $B(x,r)\subseteq\bigcap_iG_i=G$。每个 $x$ 都有这样的球，$G$ 开。若没有任何 $x\in G$，集合为空，仍开。
反例 $\bigcap_{n\ge1}(-1/n,1/n)=\{0\}$ 说明“有限”真正用在 $r>0$，不能把最小值换成可能为0的下确界后还称其为邻域半径。
''')
for n,interior in [(49,True),(50,False),(51,True),(52,False)]:
 put(n,(r'''设 $G=\bigcup_{\gamma\in\Gamma}G_\gamma$，各 $G_\gamma$ 开。每个 $G_\gamma\subseteq G$，内部单调性给 $G_\gamma^\circ\subseteq G^\circ$。因为因子开，$G_\gamma^\circ=G_\gamma$，所以每个因子都包含于 $G^\circ$。对所有因子取并得 $G\subseteq G^\circ$。内部的定义恒给 $G^\circ\subseteq G$，因此两边相等，$G$ 开。可数版本只需取 $\Gamma=\N$。
这里不是声称内部算子总保持任意并的等号，而是利用\emph{因子本身开}建立一向包含，再结合内部总不大于原集。这样避免循环使用待证开性。''' if interior else r'''设 $G=\bigcup_{\gamma\in\Gamma}G_\gamma$。任取 $x\in G$，并集定义给至少一个指标 $\gamma_0$ 使 $x\in G_{\gamma_0}$。由这个因子开，取 $r>0$ 使 $B(x,r)\subseteq G_{\gamma_0}$。再由因子包含于并集，有 $B(x,r)\subseteq G$，故 $x$ 是 $G$ 的内点。任意 $x$ 都成立，$G$ 开；若并集为空，结论也成立。
这里只使用一个见证指标 $\gamma_0$，不是为全部因子同时选统一半径，因此不论有多少个因子，都不需要有限性。这正是任意并与有限交在证明中的差别。'''))
put(54,r'''
设 $G\subseteq\R$ 非空开。按老师为 $a\in G$ 选包含它且在 $G$ 内的最大开区间 $I_a=(l_a,r_a)$，端点可为无穷。具体把所有满足 $(x,a)\subseteq G$ 的左端候选取下确界，把右端候选取上确界。因为 $G$ 开，$a$ 周围已有小区间，故 $l_a<a<r_a$。
\begin{enumerate}
\item 若 $l_a<t<a$，下确界性质保证存在候选 $x<t$ 且 $(x,a)\subseteq G$，所以 $t\in G$。若 $a<t<r_a$，上确界性质给右端候选 $u>t$ 且 $(a,u)\subseteq G$，故该 $t$ 也在 $G$ 中。因此 $I_a\subseteq G$，不是只知道端点候选附近在 $G$。
\item 若有限的 $l_a$ 也属于 $G$，开性给一个跨过 $l_a$ 的小区间，和 $I_a$ 相接后产生更靠左的候选端点，违反下确界定义；若有限右端 $r_a\in G$，跨过它的小开区间与 $I_a$ 拼接会产生大于上确界的右端候选，也矛盾。所以区间不能继续延伸。
\item 两个这样的最大区间若相交，则其并仍是开区间且在 $G$ 中，同时包含原来的点。最大性迫使两个区间相等。因此不同区间两两不交；每个 $a\in G$ 在自己的区间里，故它们的并是 $G$。
\item 每个非空开区间含有理数。固定一次有理数枚举，为每个区间选其中编号最小的有理数；不交区间不可能选到同一个有理数。于是区间族单射到可数 $\Q$，至多可数。
\end{enumerate}
''')
put(55,r'''
老师使用逐层二分网格，不是把开集写成任意相交球的并。第0层用整数格点将 $\R^N$ 分割成半开立方体 $\prod_i[m_i,m_i+1)$；各层均采用同一左闭右开约定，保证边界点只属于一块。每块二分各边得到第1层，以此得到边长 $2^{-k}$ 的第 $k$ 层；所有层的方块总数可数。
先选第0层完全落在 $G$ 内的方块。第1层只选完全落在 $G$ 内且未被已选粗方块覆盖的块，依此继续。网格相容使任意两块要么不交，要么一块包含另一块；排除已覆盖块后，最终所选块两两不交，且每块都包含于 $G$。
还须证明没有漏点。任取 $x\in G$，开性给 $r>0$ 使 $B(x,r)\subset G$。取 $k$ 使第 $k$ 层方块直径 $\sqrt N2^{-k}<r$。含 $x$ 的唯一网格块 $Q$ 中任意点距 $x$ 小于 $r$，所以 $Q\subset G$。若 $x$ 之前已被粗块覆盖，已完成；否则这块在第 $k$ 层会被选中。因此每个 $x$ 最终被覆盖，所选块的并恰好是 $G$。
半开方块本身未必开，但它们的可数不交并可以等于开集，这没有矛盾。
''')
put(57,r'''
取可数族 $\mathcal B=\{B(q,1/k):q\in\Q^N,k\in\N\}$。因为 $\Q^N$ 与 $\N$ 可数，其积可数，故球族可数。目标是任何开 $G$ 都为其中一些球的并。
任取 $x\in G$，取 $\delta>0$ 使 $B(x,\delta)\subset G$。选整数 $k>2/\delta$，所以 $2/k<\delta$；再由有理点稠密选 $q\in\Q^N$ 使 $\|x-q\|<1/k$。于是 $x\in B(q,1/k)$。对任意 $y$ 在该球内，
\[\|y-x\|\le\|y-q\|+\|q-x\|<1/k+1/k=2/k<\delta.\]
所以 $B(q,1/k)\subseteq B(x,\delta)\subseteq G$。把所有包含于 $G$ 的基球取并，一边因各球在 $G$ 中而包含于 $G$，另一边因每个 $x\in G$ 均可找到这种球而包含 $G$。故等号成立。选球时须同时保证“包含 $x$”和“整个球在 $G$ 中”，只选近的有理中心还不够。
''')
# Preserve the previously written genuinely expanded finite-cover proof, not short lecture-note bodies.
from pathlib import Path
import json
_old=json.loads((Path(__file__).resolve().parents[1]/'enhancements.json').read_text())
put(60,_old['106:60'])
put(61,r'''
设闭有界 $E\subseteq\R^N$ 被开集族 $\mathcal H$ 覆盖。若 $E$ 为空，空子族即有限子覆盖；以下非空。
\paragraph{先证存在统一正半径}
若不存在 $\delta>0$ 使每个 $x\in E$ 的球 $B(x,\delta)$ 都包含于某个覆盖成员，那么对每个整数 $n$ 可选 $x_n\in E$，其球 $B(x_n,1/n)$ 不包含于任何单个成员。$E$ 有界，取子列 $x_{n_k}\to x$；$E$ 闭使 $x\in E$。覆盖给 $H_0\ni x$，开性给 $r>0$ 使 $B(x,r)\subseteq H_0$。充分大 $k$ 时同时有 $\|x_{n_k}-x\|<r/2$ 和 $1/n_k<r/2$，所以三角不等式给
\[B(x_{n_k},1/n_k)\subseteq B(x,r)\subseteq H_0,\]
与选点矛盾。故所需统一 $\delta$ 存在。
\paragraph{再把有界集分成有限小块}
将包含 $E$ 的大立方体划成有限多个小块，使每块的\emph{直径}小于 $\delta$；欧氏情形可令边长小于 $\delta/\sqrt N$。丢掉与 $E$ 不交的块。对每个剩余块 $Q_i$ 选 $z_i\in E\cap Q_i$，统一半径性质给一个 $H_i\in\mathcal H$ 使 $B(z_i,\delta)\subseteq H_i$。块中任意 $y\in E\cap Q_i$ 距 $z_i$ 小于直径，故落在 $H_i$。有限多个块覆盖 $E$，所以这些有限 $H_i$ 也覆盖 $E$。
老师最后一步必须用块的直径而非只用边长，否则高维中同一方块两点的距离可能超过 $\delta$。
''')
put(64,r'''
\paragraph{有界性不可删}
$E=\N$ 是闭但无界集合。开区间 $U_n=(n-1/2,n+1/2)$ 覆盖 $E$。任意有限子族只含有限多个这些区间，且每个区间只含一个正整数，因此只覆盖有限多个正整数，不可能覆盖整个 $E$。所以闭性本身不足以保证有限子覆盖。
\paragraph{闭性不可删}
$E=\{1/n:n\in\N\}$ 有界但不闭，因 $1/n\to0\notin E$。老师取 $U_n=(1/(2n),3/(2n))$，每个 $1/n$ 在自己的 $U_n$ 中，所以覆盖成立。任给有限指标集 $J$，其左端点的最小值 $c=\min_{n\in J}1/(2n)>0$。选 $m>1/c$，则 $1/m<c$，小于每个所选区间的左端点，故未被覆盖。任意有限子族都如此，不能有限覆盖。
证明“没有有限子覆盖”必须对\emph{任意有限选择}都找出漏点；仅发现某一组有限区间漏点不够。
''')
put(65,r'''
设非空紧 $F\subseteq G$ 且 $G$ 开。对每个 $y\in F$，取 $r_y>0$ 使 $B(y,r_y)\subseteq G$。较小球族 $\{B(y,r_y/2):y\in F\}$ 覆盖 $F$，紧性给有限子覆盖，中心记为 $y_1,\ldots,y_m$。令 $\delta=\min_i r_{y_i}/2>0$。
现在任取位移 $h$ 满足 $\|h\|<\delta$，以及任意 $z\in F$。有限覆盖保证有某个 $i$ 使 $\|z-y_i\|<r_{y_i}/2$。因此
\[\|(z+h)-y_i\|\le\|z-y_i\|+\|h\|<r_{y_i}/2+\delta\le r_{y_i}.\]
所以 $z+h\in B(y_i,r_{y_i})\subseteq G$。$z$ 任意便得 $F+h\subseteq G$；同一 $\delta$ 对所有 $z$ 和所有小位移都有效。先用半半径覆盖、后再留下另一半容纳位移，是老师构造的目的。
若 $F=\varnothing$，结论对任意 $\delta>0$ 都成立，不必取有限半径最小值。
''')
put(66,r'''
假设 $E$ 的每个开覆盖都可有限化。\textbf{证明有界：}球族 $B(0,n)$，$n\in\N$，覆盖整个空间，当然覆盖 $E$。有限子覆盖的半径最大值为某整数 $M$，于是全部所选球在 $B(0,M)$ 内，$E\subseteq B(0,M)$，所以有界。
\textbf{证明闭：}固定任意 $y\notin E$。对每个 $x\in E$，令 $r_x=\|x-y\|/3>0$。两球 $B(x,r_x)$、$B(y,r_x)$ 不交：若有公共点 $z$，则 $\|x-y\|\le\|x-z\|+\|z-y\|<2r_x=2\|x-y\|/3$，矛盾。
球族 $\{B(x,r_x):x\in E\}$ 覆盖 $E$，取有限子覆盖中心 $x_1,\ldots,x_m$。令 $r=\min_i r_{x_i}>0$。则 $B(y,r)$ 不交每个 $B(x_i,r_{x_i})$，从而不交其并，也不交 $E$。故 $y$ 是补集的内点。每个补集点都如此，补集开，$E$ 闭。空 $E$ 本来闭有界，单独包含在结论中。
''')
put(70,r'''
令 $c$ 为抽象闭包算子，已知 $A\subseteq c(A)$、$A\subseteq B\Rightarrow c(A)\subseteq c(B)$、$c(c(A))=c(A)$、$c(\varnothing)=\varnothing$。令 $C$ 为相对全集 $S$ 的补集算子，定义 $i(A)=Cc(CA)$。按老师依次检验四条：
\begin{enumerate}
\item 因 $CA\subseteq c(CA)$，取补反转包含，$i(A)=Cc(CA)\subseteq C(CA)=A$。
\item 若 $A\subseteq B$，则 $CA\supseteq CB$，闭包单调给 $c(CA)\supseteq c(CB)$，再取补得 $i(A)\subseteq i(B)$。
\item $Ci(A)=c(CA)$，故 $i(i(A))=Cc(Ci(A))=Cc(c(CA))=Cc(CA)=i(A)$。中间一步用闭包幂等，不是把两个不同运算随意取消。
\item $i(S)=Cc(CS)=Cc(\varnothing)=C\varnothing=S$。
\end{enumerate}
反向若给内部算子 $i$ 的收缩、单调、幂等和 $i(S)=S$，定义 $c(A)=Ci(CA)$：收缩取补给扩张；两次反向包含给单调；$Cc(A)=i(CA)$ 代入给 $c(c(A))=Ci(i(CA))=c(A)$；$c(\varnothing)=Ci(S)=CS=\varnothing$。最后先后应用这两构造得到 $Cc(CA)$ 或 $Ci(CA)$，双重补集消去后恢复原算子，所以不只各构造可用，而且确为一一对应。
''')
put(72,r'''
沿用 $i(A)=Cc(CA)$ 和 $c(A)=Ci(CA)$。若 $F$ 闭，即 $c(F)=F$，则
\[i(CF)=Cc(C(CF))=Cc(F)=CF.\]
因此 $CF$ 等于自身内部，是开集。反向若 $G$ 开，即 $i(G)=G$，则
\[c(CG)=Ci(C(CG))=Ci(G)=CG,\]
故 $CG$ 闭。每个等号分别是定义、双重取补、原集合的不动性。这个证明是在抽象配对算子下成立，不必预先假设欧氏球的几何结构。
''')
put(73,r'''
令 $F=\bigcap_\gamma F_\gamma$，每个 $F_\gamma$ 满足 $c(F_\gamma)=F_\gamma$。因为 $F\subseteq F_\gamma$，单调性给 $c(F)\subseteq c(F_\gamma)=F_\gamma$ 对每个 $\gamma$ 成立。故 $c(F)\subseteq\bigcap_\gamma F_\gamma=F$。另一方面闭包扩张性恒给 $F\subseteq c(F)$。两向相同，$c(F)=F$，所以交闭。
若指标族为空，按约定交为全集 $S$，而扩张性及算子取值仍在 $S$ 内给 $c(S)=S$，结论仍成立。整个过程只使用单调、扩张两条，没有暗用有限并保持性。
''')
put(74,r'''
令 $G=\bigcup_\gamma G_\gamma$，各 $i(G_\gamma)=G_\gamma$。由 $G_\gamma\subseteq G$ 及内部单调性，$G_\gamma=i(G_\gamma)\subseteq i(G)$。对全部指标取并得 $G\subseteq i(G)$；内部收缩性给 $i(G)\subseteq G$。因此 $i(G)=G$，并集开。
空指标族的并为空，而收缩性给 $i(\varnothing)\subseteq\varnothing$，所以仍等于自身内部。与闭交证明比较：一个用闭包扩张，一个用内部收缩，两个方向均须写出。
''')
put(75,r'''
记 $H$ 为所有闭超集 $F\supseteq A$ 的交。先由闭交定理知 $H$ 闭，且 $A\subseteq H$。单调性给 $c(A)\subseteq c(H)=H$，得到一向包含。
反向使用幂等性：$c(c(A))=c(A)$，所以 $c(A)$ 是闭集；扩张性又给 $A\subseteq c(A)$，说明它本身是定义 $H$ 时所取交的成员之一。因此 $H\subseteq c(A)$。合并为 $H=c(A)$。
每条公理都有明确用途：单调性比较两闭包，扩张性确保闭超集，幂等性确保闭包自己闭。不应只用“闭包最小”这句待证结论来证明自身。
''')
put(79,r'''
任取 $x\in\overline{\overline E}$，要证 $x\in\overline E$，等价于每个 $B(x,\eps)$ 都遇到 $E$。固定任意 $\eps>0$。由 $x$ 属于闭包的闭包，取 $y\in\overline E$ 使 $\|x-y\|<\eps/2$；再由 $y\in\overline E$，取 $z\in E$ 使 $\|y-z\|<\eps/2$。于是
\[\|x-z\|\le\|x-y\|+\|y-z\|<\eps.\]
找到所需原集合点 $z$，故 $x\in\overline E$。得到 $\overline{\overline E}\subseteq\overline E$，反向是闭包扩张性，总成立，所以两者相等，$\overline E$ 闭。
关键是两次逼近使用\emph{同一给定精度}的两半，第二次选点依赖第一次选出的 $y$，不能用两个互不相关的序列直接拼接。
''')
put(80,r'''
设 $F=\bigcap_\gamma F_\gamma$。取任意 $x\in\overline F$，由欧氏闭包的序列刻画，可选 $x_n\in F$ 使 $x_n\to x$。对每个固定 $\gamma$，全部 $x_n$ 都属于 $F_\gamma$；因为它闭，序列极限 $x\in F_\gamma$。对所有 $\gamma$ 成立，所以 $x\in\bigcap_\gamma F_\gamma=F$。
故 $\overline F\subseteq F$，加扩张性得相等，$F$ 闭。这里可以固定同一条 $x_n$ 检查所有因子，因为原点列在交集中，已经同时属于所有因子；不需要为不同 $\gamma$ 另选不同点列。
''')
put(81,r'''
设 $F=\bigcup_{i=1}^m F_i$，各 $F_i$ 闭。任取点列 $x_n\in F$ 且 $x_n\to x$。给每项选一个含它的因子编号 $i(n)$。有限 $m$ 个编号中至少有一个 $i_0$ 出现无穷多次，否则全部编号各出现有限次，合起来点列只有有限项，矛盾。
将这些出现按原顺序排列为严格递增 $n_k$，则每个 $x_{n_k}\in F_{i_0}$。原列收敛使子列也趋于 $x$：任给精度，原列足够晚后都达标，子列下标最终也超过该起点。因 $F_{i_0}$ 闭，$x\in F_{i_0}\subseteq F$。所以任意 $F$ 内收敛列极限仍在 $F$，$F$ 闭。
“存在某因子含无穷多项”使用有限性，是这条证明不能照搬到无限并的确切位置。
''')
put(84,r'''
若 $S=\varnothing$，取空稠密集即可。以下设 $S\ne\varnothing$。枚举有理坐标点为 $q_1,q_2,\ldots$，定义
\[T=\{(j,k)\in\N^2:S\cap B(q_j,1/k)\ne\varnothing\}.\]
对每对 $(j,k)\in T$，选 $y_{j,k}\in S\cap B(q_j,1/k)$，令 $D=\{y_{j,k}:(j,k)\in T\}$。因为 $T\subseteq\N^2$ 可数，$D$ 是可数集的像，故至多可数，且所有选点均在 $S$。
要证 $S\subseteq\overline D$，任取 $x\in S$ 和 $\eps>0$。选 $k$ 使 $2/k<\eps$，由有理点稠密选 $q_j$ 使 $\|q_j-x\|<1/k$。于是 $x\in S\cap B(q_j,1/k)$，该交非空，保证 $(j,k)\in T$，所以相应的 $y_{j,k}$ 已被选入 $D$。三角不等式给
\[\|x-y_{j,k}\|\le\|x-q_j\|+\|q_j-y_{j,k}\|<2/k<\eps.\]
故任意邻域遇到 $D$，$x\in\overline D$。对 $S$ 内所有点成立，所以 $D$ 在 $S$ 中稠密。不能改成简单取 $S\cap\Q^N$，因为集合本身可能没有任何有理点。
''')
put(92,r'''
设 $S=\prod_{i=1}^mS_i\subseteq\R^{N_1+\cdots+N_m}$。若某因子为空，积为空，闭且紧；以下均非空。
\paragraph{闭性}取 $z_n\in S,z_n\to z$，把它写为坐标块 $z_n=(z_{1n},\ldots,z_{mn})$。每个块距离不超过总距离，所以 $z_{in}\to z_i$。因每个 $S_i$ 闭，$z_i\in S_i$；所有块均合格，故 $z\in\prod_iS_i=S$，所以积闭。
\paragraph{有界性}若因子均紧，有限维中它们闭且有界。对各因子取 $M_i$ 使 $\|z_i\|\le M_i$ 对所有 $z_i\in S_i$ 成立。于是任取积元素 $z$，
\[\|z\|^2=\sum_{i=1}^m\|z_i\|^2\le\sum_{i=1}^mM_i^2.\]
右边是固定有限数，给整个积一个共同界 $M=(\sum_iM_i^2)^{1/2}$。已证积闭又有界，Heine--Borel 给积紧。所有上界必须事先对整个因子成立，不能只为当前一点选一个界。
''')
_connected=r'''
\paragraph{连通推出区间}
若 $A\subseteq\R$ 连通却不是区间，可选 $a_1<a<a_2$，$a_1,a_2\in A$ 而 $a\notin A$。令 $A_1=A\cap(-\infty,a]$，$A_2=A\cap[a,\infty)$。它们在 $A$ 中相对闭、非空，因 $a\notin A$ 而不交，且并为 $A$，这就是非平凡闭分离，违反连通。故 $A$ 是区间。
\paragraph{区间推出连通：按老师的确界路线}
反设区间 $A=F_1\cup F_2$，其中 $F_1,F_2$ 非空、不交且相对闭。选 $a_1\in F_1,a_2\in F_2$，必要时交换名字使 $a_1<a_2$。区间性给 $[a_1,a_2]\subseteq A$。令 $s=\sup(F_1\cap[a_1,a_2])$，该集合非空有界，所以 $s$ 存在且在 $[a_1,a_2]$ 中。
由确界逼近选 $t_n\in F_1\cap[a_1,a_2]$ 使 $s-1/n<t_n\le s$，故 $t_n\to s$。$s\in A$ 且 $F_1$ 相对闭，推出 $s\in F_1$。因此 $s\ne a_2$。又 $F_2$ 相对闭且 $s\notin F_2$，存在 $r>0$ 使 $B(s,r)\cap A$ 不碰 $F_2$。选 $u$ 满足 $s<u<\min(s+r,a_2)$；它在区间 $A$ 中，只能在 $F_1$，却大于上界 $s$，矛盾。故分离不存在。
原课件采用按确界属于哪侧分情形的写法；这里把“相对闭使确界属于第一侧”和“第二侧的补集提供邻域”分成两步，正是同一矛盾。不能将相对闭直接误写为在整个实数空间闭。
'''
put(94,_connected);put(96,_connected)
put(98,r'''
全部补集、闭包、边界均相对当前空间 $X$。以下按老师的蕴含关系逐条补全。
\begin{enumerate}
\item 两个非空不交开集 $U,V$ 若并为 $X$，则 $U=X\setminus V,V=X\setminus U$，所以它们又都闭；反过来两个这样的闭集也都开。因此“不存在开分离”和“不存在闭分离”等价。
\item 非平凡 clopen 集 $A$（既开又闭，且不为空、不为全域）给分离 $A,X\setminus A$。反向分离中的每一块因互为补集都 clopen。所以连通等价于仅有平凡 clopen 集。
\item $\partial A=\overline A\setminus A^\circ$。若边界空，$\overline A\subseteq A^\circ$，结合 $A^\circ\subseteq A\subseteq\overline A$ 得三者相等，$A$ 既开又闭。反向 clopen 使闭包和内部都等于 $A$，故边界空。由第2点得到空边界判据。
\item 若 $X=A\cup B$，两块非空，且 $A\cap\overline B=B\cap\overline A=\varnothing$，则对任意 $x\in A$，$x\notin\overline B$，有邻域避开 $B$，因两块覆盖 $X$，这个邻域在 $A$ 内；故 $A$ 开。对 $x\in B$，$x\notin\overline A$ 同样给避开 $A$ 的邻域，覆盖关系使该邻域在 $B$ 中，故 $B$ 也开。反向若是开分离，两块又都闭，所以各自闭包为自身，得到上述两个交为空。
\item 若 $f:X\to\{0,1\}$ 连续且非常值，两个非空纤维 $f^{-1}(\{0\}),f^{-1}(\{1\})$ 均开（离散空间单点开），且不交并为 $X$，所以 $X$ 不连通。
\item 为补老师省掉的反向，若存在非平凡 clopen $A$，定义 $f=1_A$。离散双点空间的开集只有 $\varnothing,\{0\},\{1\},\{0,1\}$；其逆像依次为 $\varnothing,X\setminus A,A,X$，都开，所以 $f$ 连续且非常值。故“所有到双点空间的连续函数都常值”也等价于连通。
\end{enumerate}
最后一方向必须主动构造示性函数，不能从“假如函数常值则纤维平凡”倒推所有 clopen 集平凡；那会遗漏一般 clopen 集与函数之间的联系。
''')
