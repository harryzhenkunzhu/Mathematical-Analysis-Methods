BLOCKS={}
def put(n,s):BLOCKS[f'107:{n}']=s
put(9,r'''
令 $f:X\to Y$，$X,Y$ 为度量空间。要比较的五条为：(1) $f$ 连续；(2) 每个开 $G\subseteq Y$ 的逆像开；(3) 每个闭 $F\subseteq Y$ 的逆像闭；(4) $f(\overline A)\subseteq\overline{f(A)}$ 对所有 $A\subseteq X$；(5) $\overline{f^{-1}(B)}\subseteq f^{-1}(\overline B)$ 对所有 $B\subseteq Y$。这里不同横线分别在对应空间取闭包。
\paragraph{第9页：误差定义与邻域定义}
$\eps$--$\delta$ 定义中的蕴含 $d_X(x,x_0)<\delta\Rightarrow d_Y(f(x),f(x_0))<\eps$，恰好说 $f(B_X(x_0,\delta))\subseteq B_Y(f(x_0),\eps)$。任意输出邻域 $V$ 含一个这样的 $\eps$ 球，故连续给某输入邻域的像在 $V$ 中；反向令 $V$ 就是任意给定的 $\eps$ 球，输入邻域再含 $\delta$ 球，恢复误差定义。
\paragraph{(1)$\Rightarrow$(2)}任取 $x_0\in f^{-1}(G)$。$G$ 开且含 $f(x_0)$，可取 $\eps$ 球在 $G$ 中。连续性给 $\delta$ 球的像在该球中，所以 $B(x_0,\delta)\subseteq f^{-1}(G)$。每个逆像点都是内点，逆像开。
\paragraph{(2)$\Rightarrow$(1)}给 $x_0$ 及输出邻域 $V$，取开 $V'$ 满足 $f(x_0)\in V'\subseteq V$。开逆像 $f^{-1}(V')$ 含 $x_0$，故包含某输入球，且球的像在 $V'\subseteq V$。所以在 $x_0$ 连续；$x_0$ 任意，得到(1)。
\paragraph{(2)$\Rightarrow$(3)及反向}对闭 $F$，$Y\setminus F$ 开，且 $f^{-1}(Y\setminus F)=X\setminus f^{-1}(F)$。由(2)右侧开，故 $f^{-1}(F)$ 闭。反向对开 $G$ 使用闭集 $Y\setminus G$，其逆像为 $X\setminus f^{-1}(G)$，由(3)闭，故 $f^{-1}(G)$ 开。
\paragraph{(3)$\Rightarrow$(4)}固定 $A$。闭集 $\overline{f(A)}$ 的逆像 $H=f^{-1}(\overline{f(A)})$ 闭。每个 $a\in A$ 满足 $f(a)\in f(A)\subseteq\overline{f(A)}$，所以 $A\subseteq H$。闭超集包含闭包，故 $\overline A\subseteq H$。取像并按逆像定义，得到 $f(\overline A)\subseteq\overline{f(A)}$。
\paragraph{(4)$\Rightarrow$(3)}固定闭 $F$，令 $A=f^{-1}(F)$。$f(A)\subseteq F$，所以 $\overline{f(A)}\subseteq\overline F=F$。由(4)，$f(\overline A)\subseteq F$，故 $\overline A\subseteq f^{-1}(F)=A$。再由 $A\subseteq\overline A$ 得相等，逆像闭。
\paragraph{(3)$\Rightarrow$(5)}$f^{-1}(\overline B)$ 闭且包含 $f^{-1}(B)$，因此也包含后者的闭包，正是(5)。
\paragraph{(5)$\Rightarrow$(3)}令 $B=F$ 为闭集，则 $\overline{f^{-1}(F)}\subseteq f^{-1}(\overline F)=f^{-1}(F)$；配合闭包扩张得逆像闭。
\paragraph{原页还列出的(4)$\Rightarrow$(5)}令 $A=f^{-1}(B)$，由(4)及 $f(f^{-1}(B))\subseteq B$，
\[f(\overline{f^{-1}(B)})\subseteq\overline{f(f^{-1}(B))}\subseteq\overline B.\]
把像包含改写为原点属于逆像，即得(5)。
\paragraph{(5)$\Rightarrow$(4)补足原页的闭包步骤}固定 $A$，$A\subseteq f^{-1}(f(A))$，先对两边\emph{取闭包}，再用(5)于 $B=f(A)$：
\[\overline A\subseteq\overline{f^{-1}(f(A))}\subseteq f^{-1}(\overline{f(A)}).\]
因此 $f(\overline A)\subseteq\overline{f(A)}$。原页若不先取闭包，就只得到对 $A$ 的结论，无法证明(4)。至此老师列出的每条箭头均有完整理由。
''')
put(13,r'''
必要性：若 $f:S\to\R$ 连续，$(-\infty,t]$ 与 $[t,\infty)$ 闭，闭逆像判据使 $\{f\le t\}$、$\{f\ge t\}$ 闭。
充分性：假设这些集合对所有实数 $t$ 都闭。取补得到 $\{f>t\}$ 和 $\{f<t\}$ 开。任意有限端点开区间 $(a,b)$ 的逆像为 $\{f>a\}\cap\{f<b\}$，是有限开交，故开；无穷端点区间对应其中单个条件，也开。
任取实数开集 $O$，由下一条的区间分解可写 $O=\bigcup_j I_j$，则
\[f^{-1}(O)=f^{-1}(\bigcup_jI_j)=\bigcup_jf^{-1}(I_j).\]
等式由 $f(x)$ 属于并集当且仅属于某个成员给出。右边为开集的并，因此开。所有开集逆像开，故 $f$ 连续。这里将所有阈值假设变成一般开集判据的桥梁，就是区间分解与逆像保持并，不能仅验证两个方向的半直线便直接宣布结论。
''')
put(14,r'''
按老师在开集 $G$ 内定义关系：
\[a\sim b\quad\Longleftrightarrow\quad[\min(a,b),\max(a,b)]\subseteq G.\]
即连接两点的整个闭线段都在 $G$ 内。
\begin{enumerate}
\item 自反性因 $\{a\}\subset G$；对称性因线段不依赖端点顺序；若 $a\sim b,b\sim c$，前两线段的并包含 $a,c$ 间整段，所以 $a\sim c$。因此是等价关系，等价类分割 $G$。
\item 每一类是区间：若 $a,b$ 在同类，中间 $t$ 在 $[a,b]\subset G$，且 $a$ 到 $t$ 的线段也在 $G$，故 $t$ 同类。
\item 类是开区间：任取类中 $t$，$G$ 开给 $(t-r,t+r)\subset G$。其中任意 $z$ 与 $t$ 间的线段在此小区间内，所以 $z\sim t$，整个小区间在该类中。每点有内邻域，类开。
\item 不同类不交且并为 $G$，由等价类性质已得。每类选一个有理数（固定有理枚举取最早出现者），不交保证不同类所选数不同，于是类族单射到 $\Q$，至多可数。
\end{enumerate}
故 $G$ 为可数个不交开区间之并，端点允许无穷。若 $G$ 空，取空区间族，结论同样成立。
''')
put(15,r'''
设 $K$ 紧，$f:K\to Y$ 连续。若 $K=\varnothing$，像空，紧性直接成立。以下任取像集 $f(K)$ 的一个开覆盖 $\{U_\gamma\}_{\gamma\in\Gamma}$。
每个 $f^{-1}(U_\gamma)$ 在 $K$ 中相对开。任取 $x\in K$，像点 $f(x)$ 被某个 $U_\gamma$ 覆盖，所以 $x\in f^{-1}(U_\gamma)$，这些逆像确实覆盖整个 $K$。紧性给有限指标 $\gamma_1,\ldots,\gamma_m$ 仍覆盖 $K$。
要证明对应的原开集覆盖像，任取 $y\in f(K)$，选 $x\in K$ 使 $f(x)=y$。有限逆像覆盖给某个 $i$ 使 $x\in f^{-1}(U_{\gamma_i})$，即 $y=f(x)\in U_{\gamma_i}$。故 $f(K)\subseteq\bigcup_{i=1}^mU_{\gamma_i}$。原覆盖任意，得到像紧。
注意一般仅有 $f(f^{-1}(U))\subseteq U$，未必相等；老师公式中取像时使用包含已足够，不需假设满射到整个 $Y$。
''')
put(16,r'''
设 $K$ 非空紧，$f:K\to\R$ 连续。前条连续像紧给 $M=f(K)$ 非空紧，实数紧集闭有界。因此 $u=\sup M,l=\inf M$ 都为有限实数。
由上确界逼近性质，对每个 $n$ 选 $y_n\in M$ 满足 $u-1/n<y_n\le u$，则 $y_n\to u$。因 $M$ 闭，$u\in M$。按像定义存在 $x_u\in K$ 使 $f(x_u)=u$，而 $u$ 是上界，故所有 $x\in K$ 都有 $f(x)\le f(x_u)$，得到最大点。
同理选 $z_n\in M$ 使 $l\le z_n<l+1/n$，则 $z_n\to l$，闭性给 $l\in M$，再选 $x_l$ 达到它。于是最大最小都达到。
老师以“确界属于闭包，而像闭”表述的步骤，就是上述构造。不能只知道实数有确界便说取到最优值，取到这一步真正使用像闭。最优值是一个数，最优点是原定义域的点，必须在最后通过像定义选回。
''')
put(18,r'''
设 $S$ 连通，$f:S\to Y$ 连续。反设像集 $f(S)$ 不连通，则可写 $f(S)=V_1\cup V_2$，其中 $V_i$ 在像空间中相对开、非空、不交。
两逆像 $U_i=f^{-1}(V_i)$ 在 $S$ 中相对开。它们非空，因为 $V_i$ 是像的非空部分，其中任一点都有原像。若 $x$ 同时在两逆像，则 $f(x)\in V_1\cap V_2$，矛盾，故逆像不交。又每个 $x\in S$ 的像属于 $V_1$ 或 $V_2$，所以 $S=U_1\cup U_2$。这构成非平凡开分离，违反 $S$ 连通。故像连通。
相对开性不是障碍：可写 $V_i=f(S)\cap O_i$，其中 $O_i$ 在 $Y$ 中开；其逆像就是 $f^{-1}(O_i)$，所以确实开。证明没有要求像集在整个 $Y$ 中本身是开集。
''')
put(19,r'''
设连通 $X$ 上的 $f:X\to\R$ 连续，且 $f(x_1)\le\alpha\le f(x_2)$。由前条 $f(X)$ 连通；实数连通子集是区间，所以只要含两端数，就包含它们之间每个数。因此 $\alpha\in f(X)$。按像定义存在 $x\in X$ 使 $f(x)=\alpha$，正是要证的存在。
如果 $\alpha$ 恰为端点值，可直接选 $x_1$ 或 $x_2$；严格中间时用区间性。若想检查这里引用的区间性：若中间 $\alpha$ 缺失，则像在 $(-\infty,\alpha)$ 与 $(\alpha,\infty)$ 两侧均有点，交这两个开半直线会产生像的非空不交开分离，违反连通。这说明老师的一句“像必为区间”具体排除了什么。
''')
for n,lower in [(26,True),(27,False),(28,True),(29,False)]:
 if lower:
  s=r'''
定义下半连续：固定 $x_0$，每个 $\eps>0$ 存在邻域 $U$，使 $f(x)>f(x_0)-\eps$ 对所有 $x\in U$ 成立。要证它等价于每个严格上水平集 $G_t=\{x:f(x)>t\}$ 开。
\paragraph{下半连续推出开性}取 $x_0\in G_t$，间距 $f(x_0)-t>0$。选 $\eps=(f(x_0)-t)/2$，由定义得附近
\[f(x)>f(x_0)-\eps=(f(x_0)+t)/2>t.\]
所以某邻域包含于 $G_t$，每个成员是内点，$G_t$ 开。
\paragraph{开性推出下半连续}给任意 $x_0,\eps>0$，令 $t=f(x_0)-\eps$，则 $x_0\in G_t$。假设的开性给包含 $x_0$ 且在 $G_t$ 中的邻域 $U$。其中全部点都有 $f(x)>f(x_0)-\eps$，恰是定义。
最后 $\{f\le t\}=X\setminus G_t$，所以严格上水平开也等价于弱下水平闭。严格与弱符号配对必须保持，不能把 $>$ 任意换成 $\ge$。
'''
 else:
  s=r'''
上半连续定义为每个 $\eps>0$ 存在邻域 $U$，使其中 $f(x)<f(x_0)+\eps$。要证等价于 $G_t=\{x:f(x)<t\}$ 对每个 $t$ 都开。
若 $x_0\in G_t$，取正数 $\eps=(t-f(x_0))/2$。上半连续使附近 $f(x)<f(x_0)+\eps=(f(x_0)+t)/2<t$，所以 $x_0$ 是 $G_t$ 内点。由点任意，$G_t$ 开。
反向给 $x_0,\eps>0$，取 $t=f(x_0)+\eps$，开集 $G_t$ 含 $x_0$，直接为定义提供所需邻域。再取补得到弱上水平集 $\{f\ge t\}$ 闭。
也可按老师的对偶说法令 $g=-f$：$g(x)>g(x_0)-\eps$ 等价于 $f(x)<f(x_0)+\eps$，所以下半连续结论反号后正是本条。反号会翻转不等式，不能只更改定理名称不改符号。
'''
 put(n,s)
from pathlib import Path
import json
E=json.loads((Path(__file__).resolve().parents[1]/'enhancements.json').read_text())
for n in [30,33]:put(n,E[f'107:{n}'])
for n,lower in [(31,True),(34,False)]:
 if lower:
  s=r'''
先按老师的开覆盖路线证明有下界。对每个整数 $j$，开集 $U_j=\{x:f(x)>-j\}$ 是下半连续函数的严格上水平集。因为 $f$ 处处为有限实数，每个 $x$ 都满足 $f(x)>-j$ 对某个足够大的 $j$ 成立，故这些开集覆盖紧 $K$。有限子覆盖中取最大编号 $J$，由 $U_j$ 随 $j$ 递增得 $K\subset U_J$，故 $f(x)>-J$ 对全部 $x$ 成立，$m=\inf_K f$ 有限。
由确界定义，对每个 $n$ 选 $x_n\in K$ 满足 $m\le f(x_n)<m+1/n$，因此 $f(x_n)\to m$。紧性给子列 $x_{n_k}\to x_0\in K$。
固定 $\eps>0$，下半连续给 $x_0$ 的邻域 $U$，使 $f(z)>f(x_0)-\eps$ 对 $z\in U$ 成立。子列最终进入 $U$，所以尾部满足 $f(x_{n_k})>f(x_0)-\eps$。令 $k\to\infty$ 得 $m\ge f(x_0)-\eps$。因 $\eps$ 任意，$m\ge f(x_0)$。另一方面 $m$ 是下界，$m\le f(x_0)$。故相等，$x_0$ 是最小点。
注意子列的点极限属于 $K$，以及函数值沿原选择列趋于 $m$，是两个独立理由；不能由下半连续直接声称函数值连续收敛到 $f(x_0)$。
'''
 else:
  s=r'''
先用开覆盖证明上界：开水平集 $U_j=\{x:f(x)<j\}$ 随整数 $j$ 递增并覆盖 $K$，因为函数实值。紧性给有限子覆盖，取其中最大编号 $J$ 即得 $f(x)<J$ 对所有 $x\in K$。所以 $M=\sup_K f$ 为有限数。
选 $x_n\in K$ 使 $M-1/n<f(x_n)\le M$，故函数值趋于 $M$。紧性抽子列 $x_{n_k}\to x_0\in K$。任给 $\eps>0$，上半连续给邻域 $U$，其中 $f(z)<f(x_0)+\eps$；收敛子列最终在 $U$，故取函数值极限得到 $M\le f(x_0)+\eps$。精度任意使 $M\le f(x_0)$，上界定义又给 $f(x_0)\le M$，所以取到最大值。
原课件第35页 $f(x_n)\to m$ 的小写 $m$ 应修正为此处上确界 $M$。不修正就把最大化与最小化的目标混用。
'''
 put(n,s)
for n,lower in [(36,True),(37,False)]:
 s=(r'''
令 $g(x)=\sup_i f_i(x)$，每个 $f_i$ 下半连续，假设讨论点 $g(x_0)$ 有限。任给精度 $\eps>0$，上确界定义使我们能选\emph{一个固定}指标 $i_0$ 满足
\[g(x_0)-\eps/2<f_{i_0}(x_0)\le g(x_0).\]
若所有指标都不满足左不等式，$g(x_0)-\eps/2$ 就成了更小上界，矛盾。选定 $i_0$ 后，才用该函数下半连续取邻域 $U$ 使所有 $x\in U$ 都有 $f_{i_0}(x)>f_{i_0}(x_0)-\eps/2$。于是
\[g(x)\ge f_{i_0}(x)>f_{i_0}(x_0)-\eps/2>g(x_0)-\eps.\]
这正是 $g$ 下半连续。原文两次用 $\eps$ 得 $2\eps$ 也可，但需说明任意精度可先减半。证明不要求一个指标达到确界，只需逼近；也不需要无限多个邻域的交。
''' if lower else r'''
令 $g(x)=\inf_i f_i(x)$，各 $f_i$ 上半连续，$g(x_0)$ 有限。给 $\eps>0$，由下确界性质选 $i_0$ 使 $f_{i_0}(x_0)<g(x_0)+\eps/2$。该指标选好以后，上半连续给邻域 $U$ 使其中 $f_{i_0}(x)<f_{i_0}(x_0)+\eps/2$。而下确界总不大于任意成员，所以
\[g(x)\le f_{i_0}(x)<f_{i_0}(x_0)+\eps/2<g(x_0)+\eps.\]
每个精度都有这样的邻域，故 $g$ 上半连续。这里指标可以依赖 $x_0,\eps$，但在整个邻域估计中必须保持同一个 $i_0$；若先让指标任意依赖附近点，就不能调用固定函数的局部半连续性。
''')
 put(n,s)
for n,lower in [(38,True),(39,False)]:
 if lower:
  s=r'''
设 $g(x)=\min_{1\le i\le m}f_i(x)$，各 $f_i$ 下半连续。固定 $x_0,\eps>0$，为每个 $i$ 取邻域 $U_i$，其中 $f_i(x)>f_i(x_0)-\eps/2$。有限交 $U=\bigcap_{i=1}^mU_i$ 仍为 $x_0$ 邻域。对每个 $x\in U$，这组不等式对所有 $i$ 同时成立。因为 $f_i(x_0)\ge g(x_0)$，每项都有 $f_i(x)>g(x_0)-\eps/2$。有限个数的最小值也严格大于这个共同下界，于是 $g(x)>g(x_0)-\eps$。故下半连续。
有限性在两个位置使用：有限邻域交仍为邻域，以及有限个严格大于共同界的数的最小值仍严格大于它。无穷情形只能得到弱界且邻域交可能没有内点，不能照搬。
'''
 else:
  s=r'''
设 $g(x)=\max_{1\le i\le m}f_i(x)$，各 $f_i$ 上半连续。给 $x_0,\eps>0$，每个 $i$ 的半连续性给邻域 $U_i$，其中 $f_i(x)<f_i(x_0)+\eps/2$。取有限交 $U$。对其中任意 $x$ 和每个 $i$，$f_i(x)<f_i(x_0)+\eps/2\le g(x_0)+\eps/2$。取有限最大仍小于共同上界，所以 $g(x)<g(x_0)+\eps$，正是上半连续。
不是先选一个在 $x_0$ 最大的指标后只控制它，因为附近另一个指标可能变成最大；老师对全部有限指标同时取邻域正是避免此问题。
'''
 put(n,s)
for n in [40,41,42,43]:put(n,E[f'107:{n}'])
