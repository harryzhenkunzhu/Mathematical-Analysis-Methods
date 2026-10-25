BLOCKS={}
def put(ns,s):
 for n in ns:BLOCKS[f'109:{n}']=s
put([10],r'''
给有限个 $C_i\subseteq\R^N$，要证 $\sum_i\overline{C_i}\subseteq\overline{\sum_iC_i}$。若某因子空，左边空，包含直接成立。以下任取 $z\in\sum_i\overline{C_i}$。和集定义允许选 $c_i\in\overline{C_i}$ 使 $z=\sum_i c_i$。
对每个 $i$，闭包序列刻画给 $c_{i,n}\in C_i$ 且 $c_{i,n}\to c_i$。这里有限个列可以共同以 $n$ 编号，不要求它们来自同一集合。令 $z_n=\sum_i c_{i,n}$，按和定义每个 $z_n\in\sum_i C_i$。三角不等式给
\[\|z_n-z\|=\left\|\sum_i(c_{i,n}-c_i)\right\|\le\sum_i\|c_{i,n}-c_i\|\to0.\]
最后极限因为有限多个非负趋零项的和趋零。因此 $z$ 是和集内点列的极限，属于和集闭包。任意 $z$ 都如此，得到所需包含。
这不证明反向包含，也不证明原和集闭；老师两个闭包横线的位置正是结论的实质。
''')
put([11,12],r'''
设 $C_1,\ldots,C_m$ 紧。若有空因子，和集空，紧。以下均非空。
\paragraph{原页11：统一有界性}
每个紧因子有界，取 $M_i$ 使 $\|c_i\|\le M_i$ 对其全部元素成立。任意和点 $z$ 按定义可写 $z=\sum_i c_i$。三角不等式逐次应用给
\[\|z\|\le\sum_i\|c_i\|\le\sum_iM_i=:M.\]
$M$ 是事先由各因子确定的有限常数，不依赖当前 $z$，所以整个和集有界。
\paragraph{原页12：用连续像补闭性}
定义 $F:\prod_i\R^N\to\R^N$，$F(c_1,\ldots,c_m)=\sum_i c_i$。若每个坐标块趋于极限，有限和的误差满足上面相同三角估计趋零，故 $F$ 连续。有限紧积 $K=\prod_iC_i$ 紧；它在 $F$ 下的像正是集合和，因为输出恰是各因子各选一个元素相加的全部可能。
连续紧像定理给 $F(K)$ 紧，因此在有限维也闭。与前段有界性合起来，满足老师先陈述的闭有界判据；事实上连续像步骤已经直接给紧性，不必再重复推导。
绝不能把“每个 $C_i$ 闭”当作“和闭”的理由，一般闭和未必闭；原页专门用紧积连续像正是补上这项。
''')
put([13],r'''
这是老师另一条独立路线，保留全部有限次嵌套子列。任取和集内序列 $z_n$，为每项选一个分解 $z_n=\sum_{i=1}^m c_{i,n}$，其中 $c_{i,n}\in C_i$。分解可以不唯一，任取一组即可。
紧 $C_1$ 给第一坐标子列 $c_{1,n^{(1)}_k}\to c_1\in C_1$。将\emph{全部坐标及原和列}同时限制到这些下标，再用 $C_2$ 紧性从中抽子列使第二坐标收敛；第一坐标已有极限，抽子列后仍保持。继续有限 $m$ 次后得到同一最终下标 $n_k$，使所有 $c_{i,n_k}\to c_i\in C_i$。
因此
\[z_{n_k}=\sum_i c_{i,n_k}\longrightarrow\sum_i c_i=:z,\qquad z\in\sum_i C_i.\]
原页14正是这个最后有限和取极限与极限归属步骤，必须接在原页13之后，不能漏掉。因为任取和集序列都有收敛到集内的子列，度量空间序列紧判据给和集紧。
老师每一步同时保留之前各坐标极限十分重要。若独立为每个坐标抽取子列却不嵌套，可能得不到共同下标，也就无法对原和列取极限。
''')
put([17],r'''
设因子对应值域各被一个固定紧集 $T_i$ 容纳，$\Phi(x)=\sum_i\Phi_i(x)$。本节采用闭图式上半连续，紧陪域允许它与常用定义对应。
\paragraph{上半连续方向}
给 $x_n\to x_0,y_n\to y_0,y_n\in\Phi(x_n)$。逐项取分解 $y_n=\sum_i y_{i,n}$，$y_{i,n}\in\Phi_i(x_n)\subseteq T_i$。不能从和收敛直接说每个分量收敛：例如 $n+(-n)=0$。这里应使用紧 $T_i$，依次嵌套抽取有限次子列，使同一最终指标下每个 $y_{i,n_k}\to y_{i,0}$。
因子闭图式上半连续给 $y_{i,0}\in\Phi_i(x_0)$。有限和取极限使 $y_{n_k}\to\sum_i y_{i,0}$，原列收敛使此子列也趋于 $y_0$，由极限唯一 $y_0=\sum_i y_{i,0}\in\Phi(x_0)$，完成所需。
\paragraph{下半连续方向}
给 $x_n\to x_0$ 及任意 $y_0\in\Phi(x_0)$，先固定一个旧分解 $y_0=\sum_i y_{i,0}$。各因子下半连续分别给整列 $y_{i,n}\in\Phi_i(x_n)$ 趋于 $y_{i,0}$。令 $y_n=\sum_i y_{i,n}$，则可行归属与有限和极限分别给 $y_n\in\Phi(x_n)$、$y_n\to y_0$。这次不需要抽子列，因为各因子都能对给定整列输入提供逼近。
原课件上半连续段直接写出各分量的极限，省略的正是紧性与共同子列，不能把它当作代数恒等式。
''')
put([23],r'''
设两锥都含0。正半独立的定义为：若 $d_1\in C_1,d_2\in C_2$ 且 $d_1+d_2=0$，则两者均0。
若 $C_1\cap(-C_2)=\{0\}$，给这样一组相加为0的方向，有 $d_1=-d_2$，所以 $d_1$ 同时在 $C_1$ 和 $-C_2$ 中，必为0，继而 $d_2=-d_1=0$，正半独立成立。
反向假设正半独立，任取 $d\in C_1\cap(-C_2)$，则 $d\in C_1$ 且 $-d\in C_2$，相加为0；定义给 $d=0$，所以交集包含于 $\{0\}$。两锥都含0又使0属于交，因此交恰为 $\{0\}$。
负锥 $-C_2=\{-c:c\in C_2\}$ 不是补集；交集中的点表示一个方向既由第一锥向前走，也由第二锥反向走，正是会互相抵消的情况。
''')
put([25],r'''
定义截尾集 $S^M=\{x\in S:\|x\|\ge M\}$。若 $M_1\le M_2$，任何满足更强条件 $\|x\|\ge M_2$ 的点也满足较弱条件，所以 $S^{M_2}\subseteq S^{M_1}$。
令 $\Gamma(E)$ 为包含 $E$ 且含0的最小闭锥。若 $E\subseteq F$，每个含 $F$ 的闭锥也含 $E$；尤其 $\Gamma(F)$ 是 $E$ 的一个闭锥超集，由最小性 $\Gamma(E)\subseteq\Gamma(F)$。应用于截尾集，得 $\Gamma(S^{M_2})\subseteq\Gamma(S^{M_1})$。所以这族闭锥随阈值递减，其集合列极限是交 $A S=\bigcap_M\Gamma(S^M)$。
老师再写生成锥的公式时必须保留闭包：
\[\Gamma(E)=\overline{\{\alpha x:\alpha\ge0,x\in E\}}\]
对非空 $E$ 成立。理由是未闭包的非负倍乘集已为锥且含 $E$；其闭包仍为锥，因为固定倍乘连续；任意闭锥超集又必须包含这些倍乘及其闭包，所以它确为最小。若 $E$ 空，则按“含0”的约定最小锥为 $\{0\}$，须单独处理。不能把生成闭锥误当凸包，也不能漏闭包。
''')
put([29,84],r'''
本条 $C\ne\varnothing$。若 $C$ 有界，取 $M$ 使任意 $x\in C$ 有 $\|x\|\le M$。任取 $d\in C_\infty$，定义给 $x_n\in C,t_n\to+\infty$ 且 $x_n/t_n\to d$。充分大 $t_n>0$，有 $\|x_n/t_n\|\le M/t_n\to0$，所以 $d=0$。反向0确实在锥中：固定 $x\in C$，取 $x_n=x,t_n=n$，则 $x/n\to0$。故锥恰为 $\{0\}$。
反向假设锥只有0，若 $C$ 无界，可对每个 $n$ 选 $x_n\in C$ 使 $\|x_n\|>n$。令 $u_n=x_n/\|x_n\|$，范数恒1。有限维单位球面紧，存在子列 $u_{n_k}\to u$，范数连续给 $\|u\|=1$，所以 $u\ne0$。
取对应 $t_k=\|x_{n_k}\|\to\infty$，则 $x_{n_k}/t_k=u_{n_k}\to u$，定义使 $u\in C_\infty$，与只有0矛盾。因此 $C$ 有界。不能说任意无界列范数都趋无穷，第一步的逐层选点专门保证这一点。
''')
put([30],r'''
\paragraph{单调性}若 $S_1\subseteq S_2$，则每个阈值 $M$ 下 $S_1^M\subseteq S_2^M$。生成闭锥的单调性给 $\Gamma(S_1^M)\subseteq\Gamma(S_2^M)$。任取 $d\in AS_1$，它属于左侧每一项，因此属于右侧每一项，即属于 $AS_2$。故 $AS_1\subseteq AS_2$。
\paragraph{非空和集推论}设 $T\ne\varnothing$，固定一个 $a\in T$，则 $S+\{a\}\subseteq S+T$。先用下一条已证明的平移不变性 $A(S+\{a\})=AS$，再用刚证单调性，得到
\[AS=A(S+\{a\})\subseteq A(S+T).\]
若不假设 $T$ 非空，就无法选 $a$，而和集可能空，因此非空性确实参与论证。引用平移不变性时需把它视为本组随后独立证明的引理，不能拿本推论反过来证明它。
''')
_trans=r'''
任取 $d\in(C+a)_\infty$。按定义有 $z_n\in C+a,t_n\to\infty$ 且 $z_n/t_n\to d$。逐项写 $z_n=x_n+a$，其中 $x_n\in C$。则
\[\left\|\frac{x_n}{t_n}-d\right\|\le\left\|\frac{z_n}{t_n}-d\right\|+\frac{\|a\|}{t_n}\to0.\]
两项趋零的理由分别是见证序列的已知收敛、固定平移除以趋无穷标度。因此 $d\in C_\infty$，得到 $(C+a)_\infty\subseteq C_\infty$。
反向对任意 $d\in C_\infty$，取原见证 $x_n/t_n\to d$，令 $z_n=x_n+a\in C+a$。同一误差估计给 $z_n/t_n\to d$，故 $d\in(C+a)_\infty$。或者按老师写法，将第一包含中的集合换为 $C+a$、平移换为 $-a$，也得到反向。两包含合成等号。
这说明固定原点位置的改变被无穷尺度消掉，不是说原集合本身平移后相等。
'''
put([31,85],_trans)
put([32,86],r'''
老师的等价链必须展开为见证序列的双向转换：
\begin{align*}
d\in C_\infty
&\iff\exists x_n\in C,\ t_n\to\infty:\ x_n/t_n\to d\\
&\iff\exists z_n=x_n+a\in C+a,\ t_n\to\infty:\ z_n/t_n\to d\\
&\iff d\in(C+a)_\infty.
\end{align*}
中间等价不是仅靠重命名，因为表达式多出了 $a/t_n$。正向若 $x_n/t_n\to d$，则 $z_n/t_n=x_n/t_n+a/t_n\to d+0=d$；反向若 $z_n/t_n\to d$，则 $x_n=z_n-a\in C$ 且 $x_n/t_n=z_n/t_n-a/t_n\to d$。$a$ 固定保证 $a/t_n\to0$，标度保持不变，所以两方向见证都合法。
最后截尾定义与序列定义已经证明等价时，可将 $C_\infty$ 换写为 $AC$，得到原页的记号。不能只对其中一个包含验证见证转换便称为等价链。
''')
put([33,88],r'''
设 $C=\prod_{i=1}^mC_i$。若积为空，包含按相应空锥约定单独成立；以下取 $d\in C_\infty$，由定义选 $x_n=(x_{1n},\ldots,x_{mn})\in C$ 与同一 $t_n\to\infty$，满足 $x_n/t_n\to d=(d_1,\ldots,d_m)$。
对每个固定 $i$，积归属给 $x_{in}\in C_i$，坐标投影连续给 $x_{in}/t_n\to d_i$。这正是 $d_i\in(C_i)_\infty$ 的完整见证，故全部坐标合起来得到
\[d\in\prod_i(C_i)_\infty.\]
由任意 $d$ 得 $C_\infty\subseteq\prod_i(C_i)_\infty$。0方向也被此推理覆盖，无须跳过。
反向不能从各自见证直接拼接，因为不同因子的 $t_n$ 可能不相同；本条只证明包含。原页89另用截尾的证明存在错误，见其单列辨错步骤。
''')
put([35,36,90,91],r'''
设 $C=\bigcap_\gamma C_\gamma$，且 $\bigcap_\gamma(C_\gamma)_\infty=\{0\}$。若 $C$ 为空，空集本来有界；以下非空。
固定任意 $\gamma$，有 $C\subseteq C_\gamma$。渐近锥单调性给 $C_\infty\subseteq(C_\gamma)_\infty$。对所有 $\gamma$ 都成立，故
\[C_\infty\subseteq\bigcap_\gamma(C_\gamma)_\infty=\{0\}.\]
因为 $C$ 非空，固定一点并除以 $n$ 可证 $0\in C_\infty$。因此不是仅有包含，而是 $C_\infty=\{0\}$。由前条“非空集合有界当且仅渐近锥只有0”，得到 $C$ 有界。
如果按老师另一版写成截尾，零以外没有渐近方向便意味着不可能存在任意远的交集点；否则将其归一化，单位球面紧性会给一个非零方向，落在上述所有锥中，矛盾。不能直接从交锥只有0无理由写“某阈值后截尾为空”，中间正是这个有界性判据。
''')
_linear=r'''
设闭 $C\subseteq\R^N$，线性 $L:\R^N\to\R^K$ 满足 $\ker L\cap C_\infty=\{0\}$。有限维线性映射连续；例如矩阵系数的有限和给 $\|Lz\|\le M\|z\|$。
\paragraph{原页38/93：像有界迫使原像有界}
若有 $x_n\in C$ 的线性像有界，而原像列无界，取子列（重记）使 $r_n=\|x_n\|\to\infty$。单位向量 $u_n=x_n/r_n$ 再抽子列趋于单位 $u$。由渐近锥定义 $u\in C_\infty$。又
\[Lu=\lim_n L(x_n/r_n)=\lim_n(Lx_n)/r_n=0,\]
因为分子有界、分母趋无穷。故 $u\in\ker L\cap C_\infty$ 却 $\|u\|=1$，矛盾。得到所需有界性。
\paragraph{原页39/94：像闭}
取任意 $y_n\in L(C)$ 且 $y_n\to y$。每项选 $x_n\in C$ 使 $Lx_n=y_n$。收敛像列有界，上段使 $x_n$ 有界，故抽 $x_{n_k}\to x$。$C$ 闭给 $x\in C$，$L$ 连续给 $Lx=\lim_kLx_{n_k}=\lim_ky_{n_k}=y$。于是 $y\in L(C)$，像闭。原像不要求唯一，任意分解都受同一核条件约束。
\paragraph{原页40/95：容易方向 $L(C_\infty)\subseteq(L(C))_\infty$}
给 $d\in C_\infty$，取 $x_n\in C,t_n\to\infty,x_n/t_n\to d$。令 $y_n=Lx_n\in L(C)$，则 $y_n/t_n=L(x_n/t_n)\to Ld$，所以 $Ld$ 是像集的渐近方向。此方向不需要闭性及核条件。
\paragraph{原页41/96：反向，补上不能直接套用的缩放有界性}
任取 $y\in(L(C))_\infty$，选 $y_n\in L(C),t_n\to\infty,y_n/t_n\to y$，再选 $x_n\in C$ 使 $Lx_n=y_n$。需证 $x_n/t_n$ 有界；因为这些缩放点\emph{未必在 $C$ 中}，不能直接应用第一段。
反设缩放列无界，取子列使 $q_n=\|x_n\|/t_n\to\infty$，并进一步使 $u_n=x_n/\|x_n\|\to u$，$\|u\|=1$。这时 $\|x_n\|=q_nt_n\to\infty$，所以 $u\in C_\infty$，且
\[Lu=\lim_n\frac{Lx_n}{\|x_n\|}=\lim_n\frac{y_n/t_n}{q_n}=0.\]
又与核条件矛盾。故 $x_n/t_n$ 有界，可抽子列趋于 $d$。同一原点及标度满足定义，$d\in C_\infty$；连续性给 $Ld=\lim_nL(x_n/t_n)=y$。所以 $y\in L(C_\infty)$。两方向合成等号。原页略过的缩放有界证明是本定理最关键的补步。
'''
put([38,93],_linear)
_sum=r'''
假设各闭 $C_i\subseteq\R^N$ 的渐近锥正半独立：若 $d_i\in(C_i)_\infty$ 且 $\sum_i d_i=0$，则每个 $d_i=0$。若某因子空，和为空，闭性直接成立；以下非空。
令 $C=\prod_{i=1}^mC_i$，并定义线性映射 $L(x_1,\ldots,x_m)=\sum_i x_i$。有限闭积闭，且 $L(C)=\sum_iC_i$。积锥包含已给
\[C_\infty\subseteq\prod_i(C_i)_\infty.\]
若 $d=(d_1,\ldots,d_m)\in\ker L\cap C_\infty$，则每个 $d_i\in(C_i)_\infty$，同时 $\sum_id_i=Ld=0$。正半独立性强迫全部 $d_i=0$，故 $d=0$。反向0确实在该交，所以核条件正好成立。应用线性像定理，$L(C)=\sum_iC_i$ 闭。
再证明老师随后的锥包含：线性像定理给 $(L(C))_\infty=L(C_\infty)$；积锥包含经 $L$ 的单调取像给
\[L(C_\infty)\subseteq L\left(\prod_i(C_i)_\infty\right)=\sum_i(C_i)_\infty.\]
所以 $(\sum_iC_i)_\infty\subseteq\sum_i(C_i)_\infty$。最后一个等号只是求和映射的像定义，不要求在一般情形积锥等于锥的积。核条件须先验证再用定理，不能仅说 $L$ 连续便断言闭像。
'''
put([43,45,98],_sum)
put([49],r'''
设 $C=\bigcap_\gamma C_\gamma$，每个 $C_\gamma$ 凸。若交为空，凸性条件“任取交中两点”无对象，按定义空集凸。否则任取 $x,y\in C$ 及 $t\in[0,1]$。交定义使 $x,y$ 同时在每个 $C_\gamma$；对固定任意 $\gamma$，其凸性给 $tx+(1-t)y\in C_\gamma$。对所有 $\gamma$ 成立，所以该组合在交 $C$ 中。
已经验证每一对端点和每个权重，故 $C$ 凸。不必假设交闭，也不必假设指标族有限；这是纯粹逐因子全称条件的证明。
''')
put([50],r'''
\paragraph{和凸}设 $C_i$ 凸，任取 $x,y\in\sum_iC_i$，分别选分解 $x=\sum_ix_i,y=\sum_iy_i$，其中 $x_i,y_i\in C_i$。给任意 $t\in[0,1]$，各因子凸使 $z_i=tx_i+(1-t)y_i\in C_i$。有限加法分配给
\[tx+(1-t)y=t\sum_ix_i+(1-t)\sum_iy_i=\sum_i[tx_i+(1-t)y_i]=\sum_iz_i,\]
故它是合法和点。对所有端点与权重成立，和凸。
\paragraph{积凸}任取 $x=(x_i),y=(y_i)\in\prod_iC_i$。向量逐坐标运算给 $tx+(1-t)y=(tx_i+(1-t)y_i)_i$。每个坐标在对应凸因子中，所以整个向量在积中，积凸。
同一个权重 $t$ 必须用于全部坐标或分量，因为我们要证明的是\emph{原两个完整向量之间的线段}，不是分别选不相关权重得到的另一点。若某因子空，和或积为空，凸性按定义成立。
''')
put([51],r'''
设 $C$ 凸。任取 $x,y\in\overline C$ 和 $t\in[0,1]$。由闭包序列刻画，分别取 $x_n,y_n\in C$ 使 $x_n\to x,y_n\to y$。因 $C$ 凸，$z_n=tx_n+(1-t)y_n\in C$。误差估计
\[\|z_n-[tx+(1-t)y]\|\le t\|x_n-x\|+(1-t)\|y_n-y\|\to0\]
表明原集中的该点列趋于所需组合。闭包包含原集内序列的全部极限，所以 $tx+(1-t)y\in\overline C$，完成定义。
原课件开头若写“$x,y$ 在凸集 $C$ 中”，应明确这里选择的是\emph{闭包}中的端点；否则只证明原集凸，尚未涉及闭包。权重固定再取极限，不能在过程中让权重未经控制地随 $n$ 改变。
''')
put([52],r'''
设凸集 $C$ 不连通，反设有非空不交相对开集 $U,V$ 并为 $C$。选 $x\in U,y\in V$。令连续路径 $h:[0,1]\to\R^N$ 为 $h(t)=(1-t)x+ty$；凸性保证每个路径点都在 $C$，所以可看作到 $C$ 的连续函数。
令 $I_U=h^{-1}(U),I_V=h^{-1}(V)$。相对开集的连续逆像在 $[0,1]$ 中相对开。因 $h(0)=x\in U,h(1)=y\in V$，两逆像均非空；因 $U,V$ 不交，逆像不交；因每个路径点在 $C=U\cup V$，它们又覆盖整个 $[0,1]$。
于是区间被两个非空不交相对开集分离，与实区间连通矛盾。故 $C$ 连通。证明用到凸性是保证\emph{整条}连接路径在 $C$，仅知道端点在 $C$ 不能保证这一点。
''')
put([53,115],r'''
老师这一版使用截尾生成闭锥，须补足闭包逼近。设闭凸 $C$ 含0，$d\in AC$。若 $d=0$，已在 $C$。否则选足够大的阈值整数 $M$。由 $d\in\Gamma(C^M)$，可取 $z_M\in C$、$\|z_M\|\ge M$ 和 $\alpha_M\ge0$ 使
\[\|\alpha_Mz_M-d\|<1/M.\]
当 $M>\|d\|+1$ 时，$\alpha_M\|z_M\|\le\|d\|+1/M$，所以
\[0\le\alpha_M\le(\|d\|+1/M)/M<1.\]
因此 $\alpha_Mz_M=(1-\alpha_M)0+\alpha_Mz_M$ 是两个 $C$ 中端点的凸组合，在 $C$ 中。又选点误差使这些组合趋于 $d$，闭性给 $d\in C$。
原页直接说存在一个缩放点恰等于 $d$，忽略了生成\emph{闭}锥可能只含缩放极限；加上逼近与最后闭性才能严谨。保留的核心思路仍是“沿0与远点之间线段缩回”，并没有换成别的分离定理。
''')
put([54],r'''
本版改用序列式定义：给 $d\in C_\infty$，取 $z_n\in C,t_n\to+\infty$ 且 $z_n/t_n\to d$。因标度趋无穷，存在 $N$ 使 $n\ge N$ 时 $t_n\ge1$，所以 $\lambda_n=1/t_n\in[0,1]$。含0与凸性给
\[\frac{z_n}{t_n}=(1-\lambda_n)0+\lambda_nz_n\in C\qquad(n\ge N).\]
这条尾部点列全在 $C$ 中，且趋于 $d$，闭性使 $d\in C$。任取方向都如此，得到 $C_\infty\subseteq C$。
老师写“对每个 $n$ 组合都在 $C$”时，需先删去可能 $t_n<1$ 的有限项；极限不受删去有限项影响，但凸组合的合法范围不能无条件省略。含0、凸、闭分别用在端点、线段、最后极限三处。
''')
put([57],r'''
记 $S=\sum_{k=1}^m S_k$。若有空因子，两边均空；以下均非空。凸包是有限凸组合的全体。
\paragraph{原页57：$\operatorname{co}S\subseteq\sum_k\operatorname{co}S_k$}
取 $x\in\operatorname{co}S$，则 $x=\sum_{i=1}^r\lambda_i z_i$，$z_i\in S$，$\lambda_i\ge0,\sum_i\lambda_i=1$。对每个 $z_i$ 选分解 $z_i=\sum_kz_{ki}$，$z_{ki}\in S_k$。有限和可交换次序：
\[x=\sum_i\lambda_i\sum_kz_{ki}=\sum_k\left(\sum_i\lambda_i z_{ki}\right).\]
每个括号中的点由 $S_k$ 内点按非负和1权重组合，属于 $\operatorname{co}S_k$，所以 $x$ 属于右侧和集。
\paragraph{原页58--59：反向必须使用乘积权重}
取 $x=\sum_k x_k$，每个 $x_k\in\operatorname{co}S_k$。分别表示
\[x_k=\sum_{i_k=1}^{r_k}\lambda_{k i_k}z_{k i_k},\quad \lambda_{k i_k}\ge0,\quad\sum_{i_k=1}^{r_k}\lambda_{k i_k}=1.\]
不能把所有权重总和 $m$ 直接归一化，那会把点 $x$ 也除以 $m$。对每个多重指标 $I=(i_1,\ldots,i_m)$，定义 $w_I=\prod_{k=1}^m\lambda_{k i_k}$，$z_I=\sum_{k=1}^m z_{k i_k}\in S$。权重总和为
\[\sum_{i_1=1}^{r_1}\cdots\sum_{i_m=1}^{r_m}w_I=\prod_{k=1}^m\left(\sum_{i_k=1}^{r_k}\lambda_{k i_k}\right)=1.\]
再验证组合的点\emph{恰为} $x$：
\begin{align*}
\sum_Iw_Iz_I
&=\sum_{k=1}^m\sum_{i_k=1}^{r_k}\lambda_{k i_k}z_{k i_k}
\prod_{j\ne k}\left(\sum_{i_j=1}^{r_j}\lambda_{j i_j}\right)\\
&=\sum_{k=1}^m\sum_{i_k=1}^{r_k}\lambda_{k i_k}z_{k i_k}
=\sum_kx_k=x.
\end{align*}
因此 $x$ 是 $S$ 点的合法凸组合，属 $\operatorname{co}S$，得到反向包含。两个方向合成等号。这个展开保留老师第59页所有多重求和的作用，同时说明为何那些额外乘上的和都等于1，不改变原点。
''')
put([69],BLOCKS['109:25']+r'''
原课件下一页还解释为何归一化能产生方向。若 $x_n\in C$ 且 $\|x_n\|\to\infty$，令 $u_n=x_n/\|x_n\|$。这些点全在有限维单位球面，紧性给子列 $u_{n_k}\to u$，而范数连续给 $\|u\|=1$，故极限非零。取 $t_k=\|x_{n_k}\|\to\infty$，有 $x_{n_k}/t_k\to u$，所以 $u\in C_\infty$。若原列仅无界而不保证范数趋无穷，须先逐层选 $\|x_n\|>n$ 的子列，再作这一构造。
''')
put([77],r'''
设 $C\ne\varnothing$。\textbf{先验证锥性：}固定 $a\in C$，取 $x_n=a,t_n=n$，得到 $0\in C_\infty$。若 $d\in C_\infty$，有 $x_n/t_n\to d$。给任意 $\lambda>0$，新标度 $s_n=t_n/\lambda\to\infty$，同一原点列满足 $x_n/s_n=\lambda x_n/t_n\to\lambda d$，故正倍数仍在锥中；$\lambda=0$ 已单独处理。
\paragraph{原页78：闭性需要对角选取}
设 $d_j\in C_\infty,d_j\to d$。对每个 $j$，定义给一组自己的见证列 $x_{j,k}\in C,t_{j,k}\to\infty$ 且 $x_{j,k}/t_{j,k}\to d_j$。从第 $j$ 组中选一个足够晚的指标 $k(j)$，同时保证 $t_{j,k(j)}>j$ 和 $\|x_{j,k(j)}/t_{j,k(j)}-d_j\|<1/j$。令 $z_j=x_{j,k(j)}$、$s_j=t_{j,k(j)}$。则 $s_j>j\to\infty$，且
\[\|z_j/s_j-d\|\le\|z_j/s_j-d_j\|+\|d_j-d\|<1/j+\|d_j-d\|\to0.\]
所以 $z_j\in C,s_j\to\infty,z_j/s_j\to d$，恰为 $d\in C_\infty$ 的见证。每个锥内收敛列极限仍在锥内，故闭。直接把双指标都写成同一个 $n$ 而不选择 $k(j)$，不能保证同时满足精度与标度要求。
''')
put([79],r'''
因 $C\subseteq\overline C$，单调性先给 $C_\infty\subseteq(\overline C)_\infty$。反向取 $d\in(\overline C)_\infty$，有 $x_n\in\overline C,t_n\to\infty,x_n/t_n\to d$。闭包定义使每个 $n$ 可选 $z_n\in C$ 满足 $\|z_n-x_n\|<1/n$。注意选点随 $n$ 变化，且只要求指定误差内，不要求最近点存在。
充分大 $t_n>0$，误差估计给
\[\|z_n/t_n-d\|\le\|z_n-x_n\|/t_n+\|x_n/t_n-d\|<1/(nt_n)+\|x_n/t_n-d\|\to0.\]
因此原集合 $C$ 内的 $z_n$ 用同一标度也给方向 $d$，故 $d\in C_\infty$。得到反向包含，合为等号。这里不能把闭包点直接说成原集合点，补出的逼近及除标度误差正是两者之间的桥梁。
''')
put([80],r'''
先设 $C$ 为闭锥。若 $d\in C$，由锥性 $x_n=nd\in C$，取 $t_n=n$，则 $x_n/t_n=d$，所以 $d\in C_\infty$。反向若 $d\in C_\infty$，取见证 $x_n/t_n\to d$；充分大 $t_n>0$，锥性给 $x_n/t_n\in C$，闭性给极限 $d\in C$。两包含得 $C_\infty=C$。
对一般不闭锥，闭包仍是锥：若 $x_n\in C,x_n\to x$，对固定非负 $\lambda$ 有 $\lambda x_n\in C$ 且趋于 $\lambda x$，因此 $\lambda x\in\overline C$。前条已证闭包不改变渐近锥，所以
\[C_\infty=(\overline C)_\infty=\overline C.\]
原页写 $C_\infty=C$ 时必须看清右侧闭包横线；一般不闭锥只能得到闭包，不能漏掉它。
''')
put([82],r'''
设 $C\ne\varnothing$，$AC=\bigcap_{M\ge0}\Gamma(C^M)$。最小闭锥约定都含0，所以0在每项交中；固定原点除以 $n$ 又使0在序列式锥中。因此零方向单独完成，以下均取 $d\ne0$。
\paragraph{序列方向推出截尾方向}
若 $x_n/t_n\to d$，则范数趋于 $\|d\|>0$，充分大有 $\|x_n\|/t_n>\|d\|/2$，所以 $\|x_n\|\to\infty$。固定任意 $M$，最终 $x_n\in C^M$，且 $t_n>0$，因此 $x_n/t_n$ 在 $C^M$ 的非负倍乘集中，亦在其生成闭锥。这个闭锥含尾部及其极限，故 $d\in\Gamma(C^M)$。$M$ 任意，$d\in AC$。
\paragraph{截尾方向推出序列方向}
给 $d\in AC\setminus\{0\}$。对充分大的整数 $M$，因 $d$ 属于截尾\emph{闭}锥，选 $x_M\in C$，$\|x_M\|\ge M$，以及 $\alpha_M\ge0$，使 $\|d-\alpha_Mx_M\|<1/M$。当 $1/M<\|d\|/2$ 时，$\alpha_M$ 不可能0，否则误差等于 $\|d\|$。由三角不等式，
\[0<\alpha_M\le\frac{\|d\|+\|d-\alpha_Mx_M\|}{\|x_M\|}<\frac{\|d\|+1/M}{M}\to0.\]
令 $t_M=1/\alpha_M\to\infty$，则 $x_M/t_M=\alpha_Mx_M\to d$，且 $x_M\in C$，所以 $d$ 属于序列锥。两向均建立后才可在后续任意替换两种定义。
原页将属于闭包直接写成属于未闭倍乘集的地方应理解为此处的 $1/M$ 逼近，不能要求恰好表示。
''')
put([83],r'''
令 $C_N$ 为从 $C$ 中范数趋无穷点列归一化后可得到的单位极限集合。先取 $u\in C_N$，则存在 $x_n\in C,\|x_n\|\to\infty$，且 $x_n/\|x_n\|\to u$。以 $t_n=\|x_n\|$ 作为标度，定义直接给 $u\in C_\infty$；渐近锥对非负倍数封闭，所以任意 $\lambda u$ 也在其中。
反向取非零 $d\in C_\infty$，见证 $x_n/t_n\to d$。范数连续给 $r_n=\|x_n\|/t_n\to\|d\|>0$，所以 $\|x_n\|=r_nt_n\to\infty$。又
\[\frac{x_n}{\|x_n\|}=\frac{x_n/t_n}{\|x_n\|/t_n}\longrightarrow\frac d{\|d\|}=:u.\]
因此 $u\in C_N$ 且 $d=\|d\|u$，得非零方向的反向包含。原页再抽长度比例子列也可；它实际上已有正极限 $\|d\|$，故不能只写 $\lambda\ge0$ 后未经说明就除以它。
零方向需注意约定：若 $C$ 无界，则 $C_N$ 非空，取任何 $u$ 的0倍即得0；若 $C$ 非空有界，$C_N=\varnothing$，普通集合 $\{\lambda u:u\in C_N\}$ 为空，不能等于 $C_\infty=\{0\}$。需将生成锥约定额外含0，或把此等式限定于无界情形，再单独处理有界情形。
''')
put([87],r'''
设 $E\ne\varnothing$，固定一点 $a\in E$。任意 $c\in C$ 都有 $c+a\in C+E$，故 $C+a\subseteq C+E$。渐近锥单调性给 $(C+a)_\infty\subseteq(C+E)_\infty$。平移不变性又给 $(C+a)_\infty=C_\infty$，于是所需包含成立。
如直接验证见证：给 $d\in C_\infty$ 的 $c_n/t_n\to d$，点 $c_n+a\in C+E$ 且 $(c_n+a)/t_n=c_n/t_n+a/t_n\to d$。这解释原页两句引用实际如何作用，不需要令所选 $a$ 随 $n$ 改变，也不需要 $E$ 有界。
''')
put([89],r'''
原页欲证积的渐近锥包含于各因子锥的积，但其截尾推导的第一条关键等式错误：
\[\{(x_1,\ldots,x_m)\in\prod_iC_i:\|(x_1,\ldots,x_m)\|\ge M\}\ne\prod_i\{x_i\in C_i:\|x_i\|\ge M\}\]
一般不相等。例如 $(M,0)$ 的总范数达到 $M$，第二坐标却未达阈值。随后将“共同倍数缩放的积”当成“各自独立倍数缩放的积”的等号也未成立，共同标度不能凭空分开。
保留老师想要的逐分量方向结论，可在序列定义下完整修正：取 $d\in(\prod_iC_i)_\infty$，选同一标度 $t_n\to\infty$ 与 $x_n=(x_{in})\in\prod_iC_i$，使 $x_n/t_n\to d=(d_i)$。对固定 $i$，$x_{in}\in C_i$ 且投影收敛 $x_{in}/t_n\to d_i$，因此 $d_i\in(C_i)_\infty$。对全部 $i$ 成立，故 $d\in\prod_i(C_i)_\infty$。
这与前页88的合法原路线相同，是补正错误所必需的替代；不能继续沿不正确截尾等号推到结论后称其为证明。
''')
put([101],r'''
先看两个闭集 $A,B$。给任意 $z_n\in A+B,z_n\to z$，逐项选 $a_n\in A,b_n\in B$ 使 $z_n=a_n+b_n$。正半独立意味着不存在非零 $d\in A_\infty$ 同时 $-d\in B_\infty$。
若 $a_n$ 无界，先取子列使 $r_n=\|a_n\|\to\infty$，再从单位向量中抽子列使 $a_n/r_n\to d$，$\|d\|=1$。由于 $z_n$ 收敛有界，$z_n/r_n\to0$。于是
\[b_n/r_n=z_n/r_n-a_n/r_n\to-d.\]
同一标度 $r_n\to\infty$ 给 $d\in A_\infty,-d\in B_\infty$，它们相加为0却不为零，违反正半独立。因此 $a_n$ 有界。抽子列 $a_{n_k}\to a$，$A$ 闭使 $a\in A$；对应 $b_{n_k}=z_{n_k}-a_{n_k}\to z-a$，$B$ 闭使 $z-a\in B$。所以 $z=a+(z-a)\in A+B$，和闭。
老师说一般情形归纳，还须检查中间和的条件。若已知前 $m-1$ 个和闭且其渐近锥包含于前 $m-1$ 个锥之和，则中间和方向 $d$ 与最后方向 $e$ 抵消时，把 $d$ 分解为各旧锥方向，整体正半独立使所有分量及 $e$ 为0。因此二集条件可用。中间和的渐近锥包含可由前面的积集加求和线性映射定理建立。这样归纳才不是未检查条件的一句话。
''')
put([106],r'''
定义强方向集合 $C^1_\infty$：给任意标度 $t_n\to\infty$，都能找到 $z_n\in C$ 使 $z_n/t_n\to d$。显然强集合包含于普通渐近锥，因为可以特取 $t_n=n$。
反向设非空凸 $C$，给 $d\in C_\infty$，选一组旧见证 $x_k/s_k\to d$，$s_k\to\infty$。固定 $a\in C$，令 $u_k=(x_k-a)/s_k$，则 $u_k\to d$，且 $a+s_ku_k=x_k\in C$。
现在给\emph{任意另一条}标度 $t_n\to\infty$。对每个 $n$，选 $k(n)\ge n$ 且 $s_{k(n)}\ge t_n$；这由 $s_k\to\infty$ 保证。令
\[z_n=a+t_nu_{k(n)}=\left(1-\frac{t_n}{s_{k(n)}}\right)a+\frac{t_n}{s_{k(n)}}x_{k(n)}.\]
比例在 $[0,1]$，两端点在 $C$，凸性给 $z_n\in C$。又 $k(n)\to\infty$，所以
\[z_n/t_n=a/t_n+u_{k(n)}\to0+d=d.\]
任意标度均构造出见证，故 $d\in C^1_\infty$，两方向相等。选 $k(n)\ge n$ 的条件保证取到的方向近似确实越来越精确，而不能仅选任意满足大标度的一项后固定不动。
''')
put([108],r'''
已由前面的对角论证知道 $C_\infty$ 闭且为锥；本条只需补凸性，但不能据原集合凸就直接宣布极限方向也凸。取任意 $d_1,d_2\in C_\infty$ 及 $\lambda\in[0,1]$。
前条非空凸集渐近正则允许我们对\emph{共同}标度 $t_n=n$ 分别选 $x_{1n},x_{2n}\in C$，使 $x_{in}/n\to d_i$。若只用普通定义，各方向本来的标度未必相同，这正是先证正则性的目的。
令 $z_n=\lambda x_{1n}+(1-\lambda)x_{2n}$。凸性给 $z_n\in C$，且有限线性运算保极限：
\[z_n/n=\lambda(x_{1n}/n)+(1-\lambda)(x_{2n}/n)\to\lambda d_1+(1-\lambda)d_2.\]
用序列锥定义得到这个凸组合也在 $C_\infty$。因端点与权重任意，锥凸。闭、锥、凸分别来自不同论证，不能把它们视为同一性质。
''')
put([110],r'''
定义 $\operatorname{rec}C=\{d:\forall a\in C,\forall t\ge0,a+td\in C\}$。先仅设 $C$ 非空。
\paragraph{衰退方向总是渐近方向}
若 $d\in\operatorname{rec}C$，固定 $a\in C$，令 $x_n=a+nd\in C$，$t_n=n$。则 $x_n/t_n=a/n+d\to d$，故 $d\in C_\infty$。
\paragraph{闭凸时反向成立}
设 $C$ 另闭凸，$d\in C_\infty$，选 $x_n\in C,s_n\to\infty,x_n/s_n\to d$。要证衰退条件，必须\emph{任取}基点 $a\in C$ 及固定长度 $t>0$。充分大 $s_n\ge t$，比例 $t/s_n\in[0,1]$，所以
\[z_n=\left(1-\frac t{s_n}\right)a+\frac t{s_n}x_n\in C.\]
而 $z_n=a+t(x_n/s_n)-ta/s_n\to a+td$。闭性给 $a+td\in C$。$t=0$ 时是原点 $a$，自动成立；基点与长度任意，所以 $d\in\operatorname{rec}C$。
两包含合成 $\operatorname{rec}C=C_\infty$。若只假设凸而不闭，最后从极限回到集合内这一步不能做；原页末句此时只能对 $\overline C$ 说 $\operatorname{rec}(\overline C)=(\overline C)_\infty=C_\infty$，不能去掉闭包横线。
''')
put([112],r'''
令 $C=([0,1)\times[0,\infty))\cup\{(1,0)\}$。先算衰退锥。若 $d=(d_1,d_2)$ 是衰退方向，从任意基点沿它走所有长度都须保持第一坐标在 $[0,1]$。若 $d_1>0$，从 $(0,0)$ 走足够远会超过1；若 $d_1<0$，从 $(0,0)$ 立即变负。因此 $d_1=0$。
若 $d_2<0$，从 $(0,0)$ 走后第二坐标负；若 $d_2>0$，从 $(1,0)$ 走到 $(1,td_2)$，该点第一坐标恰1而第二坐标正，不在 $C$。故 $d_2=0$，于是 $\operatorname{rec}C=\{0\}$，不是原页写的空集，因为0方向永远合法。
再算渐近锥：若 $(u_n,v_n)\in C,t_n\to\infty$，第一坐标 $0\le u_n\le1$，所以任何缩放极限第一坐标都0；第二坐标 $v_n\ge0$，极限不可能负，故 $C_\infty\subseteq\{(0,b):b\ge0\}$。反向给任意 $b\ge0$，取 $(u_n,v_n)=(0,nb)\in C$、$t_n=n$，缩放恒为 $(0,b)$，故该射线全在渐近锥中。
所以渐近锥为竖直非负射线，而非原页写的整条直线。这严格显示闭性删除后两个锥确可不同。
''')
put([113],r'''
设非空闭凸 $C$。0在渐近锥中，所以对任意 $c\in C$，$c=c+0\in C+C_\infty$，得到 $C\subseteq C+C_\infty$。
反向任取 $x\in C+C_\infty$，写 $x=c+d$，$c\in C,d\in C_\infty$。取方向见证 $z_n\in C,t_n\to\infty,z_n/t_n\to d$。充分大 $t_n\ge1$，故
\[w_n=(1-1/t_n)c+(1/t_n)z_n\in C\]
为合法凸组合。且 $w_n=c-c/t_n+z_n/t_n\to c+d=x$。闭性给 $x\in C$。两包含证等号。
这保留老师的直接凸组合路线，即使已经证明衰退锥相等也不将本条压缩成“由定义显然”。凸性用来给每个 $w_n$ 归属，闭性用来给最终 $x$ 归属，两个步骤不能混成一句。
''')
put([114],r'''
假设 $C$ 闭凸且 $0\in C$。由上一命题 $C+C_\infty=C$。任取 $d\in C_\infty$，因 $0\in C$，和集定义给 $0+d\in C+C_\infty=C$。所以 $d\in C$，得到 $C_\infty\subseteq C$。
这是老师本页实际给的短推论，长度虽短但逻辑已全：明确选任意方向、使用0作为原集合点、代入已证和集恒等式，再返回包含结论。它无需另起一条新的完整衰退锥证明。
''')
put([117],r'''
设非空闭凸 $S$，固定 $a\in S$，令 $D_a=\bigcap_{\lambda>0}\lambda(S-a)$。老师先描述 $a+D$ 能完全留在 $S$ 中的最大锥，再给此交表达式。
\paragraph{第一部分：交等于从 $a$ 出发的全部可行射线方向}
对任意 $d$，$d\in D_a$ 等价于对每个 $\lambda>0$，$d/\lambda\in S-a$，即 $a+d/\lambda\in S$。以 $t=1/\lambda$ 重命名，正好是 $a+td\in S$ 对所有 $t>0$；$t=0$ 由 $a\in S$ 补上。这个方向集含0，且非负倍数仍保持整条射线，所以确为锥。任何 $a+C'\subseteq S$ 的锥中方向 $d$ 都满足 $a+td\in S$，因而 $C'\subseteq D_a$；而 $a+D_a\subseteq S$，所以它就是最大锥。原页反向直接从点在交中说整射线在交中，缺的正是这个对任意 $\lambda$ 的变量替换。
\paragraph{第二部分：基点无关，补足原页未经论证的等价}
给 $d\in D_a$ 与任意另一基点 $b\in S$，要证对每个固定 $t>0$ 都有 $b+td\in S$。取 $T\to\infty$ 且 $T\ge t$，由原射线 $a+Td\in S$ 及凸性，
\[z_T=(1-t/T)b+(t/T)(a+Td)\in S.\]
展开 $z_T=b+td+(t/T)(a-b)\to b+td$，闭性给极限在 $S$。因此 $d\in D_b$；交换 $a,b$ 得反向，故 $D_a=D_b$。原页只写 $a+\R_+d\subset S\iff b+\R_+d\subset S$ 而没有理由，这段凸组合极限就是不可省略的证明。
\paragraph{第三部分：与渐近锥一致}
若 $d\in D_a$，取 $x_n=a+nd\in S,t_n=n$，则 $x_n/t_n\to d$，故 $D_a\subseteq S_\infty$。反向给 $d\in S_\infty$，取 $x_n/t_n\to d$，对任意固定 $t>0$ 以 $(1-t/t_n)a+(t/t_n)x_n$ 作凸组合，取极限得到 $a+td\in S$，故 $d\in D_a$。这个步骤正是截尾与射线之间的逻辑桥梁，不能把“在生成闭锥中”直接当成“原集合包含整条射线”。
''')
