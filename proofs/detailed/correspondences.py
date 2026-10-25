from pathlib import Path
import json
E=json.loads((Path(__file__).resolve().parents[1]/'enhancements.json').read_text())
BLOCKS={}
def put(ns,s):
 for n in ns:BLOCKS[f'108:{n}']=s
for n in [11,12,47,63,64,65,66,82,83]:put([n],E[f'108:{n}'])
put([14,40],r'''
设 $\Phi(x)=\prod_{i=1}^m\Phi_i(x)$，各因子有闭图。取任意输入列 $x_k\to x$，及输出列 $y_k\in\Phi(x_k)$，假设 $y_k\to y$。把输出写为有限坐标块 $y_k=(y_{1k},\ldots,y_{mk})$，$y=(y_1,\ldots,y_m)$。
积的归属定义给 $y_{ik}\in\Phi_i(x_k)$ 对每个 $i,k$ 成立。乘积空间收敛给 $y_{ik}\to y_i$；具体在欧氏范数下块距离不超过总距离。于是固定任意 $i$，三条条件 $x_k\to x,y_{ik}\to y_i,y_{ik}\in\Phi_i(x_k)$ 允许使用该因子的闭图性，得到 $y_i\in\Phi_i(x)$。
对全部有限坐标都如此，积的定义给 $y\in\prod_i\Phi_i(x)=\Phi(x)$，所以积图闭。第14页采用共同紧陪域背景下的闭图式上半连续，第40页直接说闭对应，二者在各自约定下使用的是同一条逐坐标推理。不能只说“每坐标连续所以积连续”，这里各因子是集合值，并非单值坐标函数。
''')
put([19],r'''
设 $\Phi$ 在 $x_0$ 非空紧值且连续，$f$ 联合连续，$g(x)=\max_{y\in\Phi(x)}f(x,y)$。极值定理保证每个最大值存在。老师分下、上两个方向，但原页直接写未必存在的数列极限，并把旧最大值与任意旧可行值混同。下面保留“可行逼近＋最优点子列”的路线逐步修正。
\paragraph{先证下半连续}
任取 $x_n\to x_0$。在旧可行集选\emph{一个最大点} $y_0\in\Phi(x_0)$，使 $f(x_0,y_0)=g(x_0)$。下半连续给 $y_n\in\Phi(x_n)$ 且 $y_n\to y_0$。联合连续给 $f(x_n,y_n)\to f(x_0,y_0)=g(x_0)$。因 $y_n$ 可行，$g(x_n)\ge f(x_n,y_n)$。任给 $\eps>0$，右侧最终大于 $g(x_0)-\eps$，所以 $g(x_n)$ 也最终如此，等价于 $\liminf_n g(x_n)\ge g(x_0)$。
\paragraph{再证上半连续}
若上半连续不成立，可从某输入趋近列选子列（重记为 $x_n$）及固定 $\eps_0>0$，使 $g(x_n)\ge g(x_0)+\eps_0$ 对每项成立。对每个 $n$ 选最大点 $z_n\in\Phi(x_n)$，故 $f(x_n,z_n)=g(x_n)$。
紧值上半连续的序列紧性保证存在子列 $z_{n_k}\to z_0\in\Phi(x_0)$。在本节共同紧陪域中，这是先抽输出子列再用闭图；一般紧值上半连续版本可由紧输入列的紧像得到同样结论。连续性给
\[g(x_{n_k})=f(x_{n_k},z_{n_k})\longrightarrow f(x_0,z_0)\le g(x_0).\]
但每项至少 $g(x_0)+\eps_0$，其极限也至少这个数，矛盾。故上半连续成立。两方向合起来，对任意精度附近均有 $g(x_0)-\eps<g(x)<g(x_0)+\eps$，所以连续。
这里仅有 $f(x_0,z_0)\le g(x_0)$，不能未经证明写成相等；这是原页的重要跳步。
''')
put([20],r'''
沿用前条已证连续最优值 $g$。定义 $M(x)=\{y\in\Phi(x):f(x,y)=g(x)\}$。
\paragraph{非空与紧值}在固定 $x$，$f(x,\cdot)$ 连续，非空紧集 $\Phi(x)$ 上最大值达到，所以 $M(x)\ne\varnothing$。等值集 $\{y:f(x,y)=g(x)\}$ 闭，与紧 $\Phi(x)$ 相交为紧，故 $M(x)$ 紧。
\paragraph{验证老师抽子列的每一步}给 $x_n\to x_0$ 及任意 $y_n\in M(x_n)$。因 $M(x_n)\subseteq\Phi(x_n)$，可行对应的紧值上半连续性给子列 $y_{n_k}\to y_0\in\Phi(x_0)$。最优性给每个 $k$ 的等式 $f(x_{n_k},y_{n_k})=g(x_{n_k})$。联合连续使左边趋于 $f(x_0,y_0)$，前条的 $g$ 连续使右边趋于 $g(x_0)$。同一实数列的两种极限相等，所以 $f(x_0,y_0)=g(x_0)$。连同可行性，得到 $y_0\in M(x_0)$。
\paragraph{为什么这足以推出上半连续}若存在开 $G\supseteq M(x_0)$ 但附近总有最优点逃出，可取 $x_n\to x_0,y_n\in M(x_n)\setminus G$。按前段抽子列，极限 $y_0\in M(x_0)\subset G$；$G$ 开使收敛子列最终进入 $G$，与每项都逃出矛盾。因此上半连续。这个最后的反证把序列性质连回定义，不能只写“所以”而不解释。
''')
put([21],r'''
可行对应恒为 $\Phi(x)=[0,1]$，目标 $f(x,y)=xy$，参数 $x\in[0,1]$。固定 $x>0$，若 $y<1$，则 $xy<x=x\cdot1$，所以唯一最大点为1，$M(x)=\{1\}$；若 $x=0$，所有 $y$ 的目标都0，所以 $M(0)=[0,1]$。
选旧最优点 $y_0=0\in M(0)$。取输入列 $x_n=1/n\to0$。任何选择 $y_n\in M(x_n)$ 都只能为1，因此不能趋于0。按下半连续的序列定义，旧选择0无法逼近，故 $M$ 在0不下半连续。
用开集语言同样看见：$G=(-1/4,1/4)$ 遇到 $M(0)$，却不遇到任何 $x>0$ 的 $M(x)=\{1\}$。所以附近持续相交条件失败。这并不与上半连续矛盾：所有附近输出1仍在旧值集 $[0,1]$ 中。
''')
for ns,upper in [([29],False),([32],True)]:
 if not upper:
  s=r'''
固定非空值对应。记 $\Phi^-(G)=\{x:\Phi(x)\cap G\ne\varnothing\}$，$\Phi^+(F)=\{x:\Phi(x)\subseteq F\}$。
\paragraph{(1)$\Rightarrow$(2)}下半连续假设下，任取开 $G$ 及 $x_0\in\Phi^-(G)$，则 $\Phi(x_0)$ 遇到 $G$。定义给 $x_0$ 邻域 $U$，使每个 $x\in U$ 的值集仍遇到 $G$，即 $U\subseteq\Phi^-(G)$。每个成员有内邻域，逆像开。
\paragraph{(2)$\Rightarrow$(1)}反过来若所有开下逆像开，给定 $G$ 遇到 $\Phi(x_0)$，则 $x_0\in\Phi^-(G)$，该开逆像本身就是所需邻域，附近每点的值集都遇到 $G$。
\paragraph{(2)$\Leftrightarrow$(3)}对闭 $F$，$T\setminus F$ 开，且
\begin{align*}
x\notin\Phi^+(F)&\iff\exists y\in\Phi(x):y\notin F\\
&\iff\Phi(x)\cap(T\setminus F)\ne\varnothing\\
&\iff x\in\Phi^-(T\setminus F).
\end{align*}
故 $S\setminus\Phi^+(F)=\Phi^-(T\setminus F)$。于是开下逆像性质等价于闭集的上逆像闭。反向给任意开 $G$ 令 $F=T\setminus G$，同一公式恢复开性。空值情形须遵守原有效定义域约定。
'''
 else:
  s=r'''
上逆像 $\Phi^+(G)=\{x:\Phi(x)\subseteq G\}$。若上半连续，任取其成员 $x_0$，$G$ 是包含整个旧值集的开集，定义给邻域 $U$ 使 $\Phi(x)\subseteq G$ 对 $x\in U$ 成立，即 $U\subseteq\Phi^+(G)$，所以该逆像开。反向若开上逆像总开，当 $G\supseteq\Phi(x_0)$ 时，包含 $x_0$ 的开逆像本身就是定义所需邻域。
要换成闭集判据，固定闭 $F$，逐步取否定：
\begin{align*}
x\notin\Phi^-(F)&\iff\neg[\exists y\in\Phi(x),y\in F]\\
&\iff\forall y\in\Phi(x),y\notin F\\
&\iff\Phi(x)\subseteq T\setminus F\\
&\iff x\in\Phi^+(T\setminus F).
\end{align*}
所以 $S\setminus\Phi^-(F)=\Phi^+(T\setminus F)$。右侧开当且仅左侧所补的 $\Phi^-(F)$ 闭。所有闭 $F$ 与所有开 $T\setminus F$ 一一对应，故两个判据等价。
“整体在内”与“至少一点相交”是两种不同逆像，老师的两组等价证明必须保留这种区别。
'''
 put(ns,s)
put([34],r'''
设 $K$ 紧，$\Phi$ 紧值且上半连续。要证 $\Phi(K)=\bigcup_{x\in K}\Phi(x)$ 紧，任取其开覆盖 $\mathcal G$。若 $K$ 或像为空，有限覆盖直接成立，以下非空。
\begin{enumerate}
\item 固定 $x\in K$。$\mathcal G$ 也覆盖紧 $\Phi(x)$，故能选有限成员 $G_{x,1},\ldots,G_{x,m_x}$ 覆盖这个值。令 $V_x=\bigcup_jG_{x,j}$，它开且包含 $\Phi(x)$。
\item 上半连续给输入邻域 $U_x$ 使 $\Phi(z)\subseteq V_x$ 对所有 $z\in U_x$ 成立。这把对一个值集的有限覆盖扩展成对附近全部值集的控制。
\item $\{U_x:x\in K\}$ 覆盖紧 $K$，再选有限 $U_{x_1},\ldots,U_{x_r}$ 覆盖 $K$。
\item 任取 $y\in\Phi(K)$，选 $z\in K$ 使 $y\in\Phi(z)$；再选 $i$ 使 $z\in U_{x_i}$，则 $y\in V_{x_i}$，因而属于其某个原覆盖成员 $G_{x_i,j}$。
\end{enumerate}
所以从原覆盖中一共选出的 $\sum_{i=1}^r m_{x_i}$ 个成员覆盖像，数量有限。这里有两次有限化：每个紧输出值一次，整个紧输入集再一次，缺少任一次都不能声称最后只需有限成员。
''')
put([39],r'''
图定义为 $G(\Phi)=\{(x,y):y\in\Phi(x)\}$。度量空间中集合闭当且仅所有集内收敛序列的极限仍在集合内。
假设图闭，给 $x_n\to x_0,y_n\to y_0$ 且 $y_n\in\Phi(x_n)$。最后一条件改写为 $(x_n,y_n)\in G$；前两条件等价于乘积收敛 $(x_n,y_n)\to(x_0,y_0)$。闭性给 $(x_0,y_0)\in G$，又改写为 $y_0\in\Phi(x_0)$。
反过来假定上述坐标序列条件。取任意图内收敛列 $(x_n,y_n)\to(x_0,y_0)$，逐坐标提取前提并应用条件，就得极限仍在图，故图闭。两个方向都只是严格使用同一图成员等价，证明不要求先替输出列抽子列；输出收敛是本条已给的前提。
''')
put([41],r'''
固定输入 $x$，任取值集内序列 $y_n\in\Phi(x)$ 且 $y_n\to y$。为使用闭图定义，必须提供一条也收敛的输入列，所以令 $x_n=x$ 对所有 $n$。常数列显然趋于 $x$，且 $y_n\in\Phi(x_n)$。闭图条件给 $y\in\Phi(x)$。因此每个值集内收敛序列的极限仍在值集中，值集闭。
这只证明闭图推出闭值，反向一般不成立。单值跳跃函数的每个值集都是闭单点，但图可能漏掉跳跃处的极限点。不要把本条的单向蕴含倒过来使用。
''')
put([42],r'''
定义 $\Phi(x)=\{y\in T:f(x,y)\le0\}$，其中 $f$ 在 $S\times T$ 联合连续。取 $x_n\to x,y_n\to y,y_n\in\Phi(x_n)$。由归属定义，$f(x_n,y_n)\le0$ 对每个 $n$ 成立。联合连续使函数值趋于 $f(x,y)$，不等式保极限给 $f(x,y)\le0$，即 $y\in\Phi(x)$。这证明图闭。
原页的距离球例子令 $f(x,y)=d(x,y)-\lambda(x)$，其中 $\lambda$ 连续。距离函数联合连续，因为
\[|d(x_n,y_n)-d(x,y)|\le d(x_n,x)+d(y_n,y)\to0.\]
所以 $f$ 也连续，且 $\Phi(x)=\{y:d(x,y)\le\lambda(x)\}$，正好套入上面已经逐步证明的结论。半径若为负可能空值，但空值不妨碍图闭，只影响非空值的另一个条件。
''')
put([43],r'''
令 $\Phi(x)=\bigcap_{\lambda\in\Lambda}\Phi_\lambda(x)$，每个因子图闭。取 $x_n\to x_0,y_n\to y_0,y_n\in\Phi(x_n)$。交定义给 $y_n\in\Phi_\lambda(x_n)$ 对每个 $n$ 及每个 $\lambda$ 成立。
固定一个任意 $\lambda$，用其闭图性得到 $y_0\in\Phi_\lambda(x_0)$。因为 $\lambda$ 任意，这个极限同时在全部因子中，所以 $y_0\in\bigcap_\lambda\Phi_\lambda(x_0)=\Phi(x_0)$，证明交图闭。
没有在无限多个因子间取邻域交，因此任意指标集都允许。交值可能为空，本条只保证图闭，不会凭空保证每点存在共同输出。
''')
put([44],r'''
令 $\Phi(x)=\bigcup_{i=1}^m\Phi_i(x)$，各因子图闭。给 $x_n\to x_0,y_n\to y_0,y_n\in\Phi(x_n)$。对每个 $n$ 选一个编号 $i(n)$ 使 $y_n\in\Phi_{i(n)}(x_n)$。有限个编号至少一个 $i_0$ 出现无穷多次；按这些出现的顺序取严格递增 $n_k$。
此时 $y_{n_k}\in\Phi_{i_0}(x_{n_k})$，同时两子列仍趋于 $x_0,y_0$。由这个固定因子的闭图性 $y_0\in\Phi_{i_0}(x_0)\subseteq\Phi(x_0)$。因此并对应图闭。
原页若直接说所有项都在同一因子并不正确，必须先取子列。有限性恰好用在抽屉原理，任意无限闭图并不保证图闭。
''')
put([45],r'''
取 $x_n\to x_0,y_n\to y_0,y_n\in\Phi(x_n)$，要证 $y_0\in\Phi(x_0)$。反设不在。紧值 $K=\Phi(x_0)$ 闭，因此 $d=\operatorname{dist}(y_0,K)>0$；在度量空间里若距离为0，选 $K$ 点以误差 $1/n$ 逼近会使 $y_0$ 落入闭 $K$，矛盾。若旧值为空，直接用开空邻域的上半连续性排除附近有选择的情形。
令 $V=\{y:\operatorname{dist}(y,K)<d/3\}$，它开且含 $K$。上半连续给输入邻域 $U$ 使 $\Phi(x)\subset V$ 对 $x\in U$ 成立。由于 $x_n\to x_0$，最终 $y_n\in V$。但 $y_n\to y_0$，最终 $\|y_n-y_0\|<d/3$，而距离三角估计给 $\operatorname{dist}(y_n,K)\ge d-\|y_n-y_0\|>2d/3$，与 $y_n\in V$ 矛盾。故图闭。
老师使用“两个不交邻域”时，具体可以用这两个半径构造；不能只凭值集紧就断言任意输出列收敛，本条的输出收敛是已给前提。
''')
put([51],r'''
设陪域 $T$ 紧且各 $\Phi(x)$ 闭，因此每个值是紧集的闭子集，故紧。若 $\Phi$ 上半连续，前条紧值上半连续推出闭图。
反向假设图闭。定义常对应 $\Delta(x)=T$。它紧值；对任何开集 $G\supseteq\Delta(x_0)=T$，有 $\Delta(x)\subseteq G$ 对所有输入都成立，所以常对应上半连续。因为值本来都在 $T$ 内，逐点有 $\Phi=\Phi\cap\Delta$。对闭图 $\Phi$ 与紧值上半连续 $\Delta$ 用前面的交对应定理，得到交上半连续，亦即原对应上半连续。
这里没有使用“闭值推出闭图”；闭图是本方向假设，闭值只帮助保证紧值。两者的角色必须区分。
''')
put([52],r'''
设 $S$ 非空紧，$\Phi:S\rightrightarrows S$ 非空紧值上半连续。令 $K_0=S,K_{n+1}=\Phi(K_n)$。
\begin{enumerate}
\item 非空值使每个非空 $K_n$ 的像非空；紧像定理使像紧，故归纳得到全部 $K_n$ 非空紧。
\item 因自对应，$K_1\subseteq K_0$。集合像单调，所以若 $K_n\subseteq K_{n-1}$，取像给 $K_{n+1}\subseteq K_n$。故它们递减。
\item 非空紧集套的交 $K=\bigcap_{n\ge0}K_n$ 非空紧。因 $K\subseteq K_n$，取像得 $\Phi(K)\subseteq K_{n+1}$ 对所有 $n$ 成立，所以 $\Phi(K)\subseteq K$。
\item 反向任取 $a\in K$。因 $a\in K_{n+1}=\Phi(K_n)$，对每个 $n$ 取 $x_n\in K_n$ 使 $a\in\Phi(x_n)$。全部 $x_n\in S$，紧性抽子列 $x_{n_j}\to x\in S$。固定任意 $m$，充分大 $j$ 时 $n_j\ge m$，故 $x_{n_j}\in K_m$；$K_m$ 闭使 $x\in K_m$，对每个 $m$ 都成立，$x\in K$。
\item 输出常数列 $a$ 也收敛，闭图性与 $a\in\Phi(x_{n_j})$ 给 $a\in\Phi(x)\subseteq\Phi(K)$。所以 $K\subseteq\Phi(K)$，合得 $K=\Phi(K)$。
\end{enumerate}
不变\emph{集}不等于不动\emph{点}：本条没有证明某个 $x\in K$ 必满足 $x\in\Phi(x)$，不能当作 Kakutani 的证明。
''')
put([55,56],r'''
设 $\Phi_1:S\rightrightarrows T,\Phi_2:T\rightrightarrows Z$ 都下半连续。复合按集合像定义：$\Psi(x)=\bigcup_{y\in\Phi_1(x)}\Phi_2(y)$。
\paragraph{老师第一种证明：开集的下逆像}
任取 $Z$ 中开集 $G$，固定任意 $x$，逐层展开：
\begin{align*}
x\in\Psi^-(G)&\iff\exists z\in G,\exists y\in\Phi_1(x):z\in\Phi_2(y)\\
&\iff\exists y\in\Phi_1(x):\Phi_2(y)\cap G\ne\varnothing\\
&\iff\Phi_1(x)\cap\Phi_2^-(G)\ne\varnothing\\
&\iff x\in\Phi_1^-(\Phi_2^-(G)).
\end{align*}
所以 $\Psi^-(G)=\Phi_1^-(\Phi_2^-(G))$。先由 $\Phi_2$ 下半连续知内层集合开，再由 $\Phi_1$ 下半连续知外层逆像开。对任意开 $G$ 都成立，故复合下半连续。
\paragraph{老师第二种证明：闭集的上逆像}
对闭 $F\subseteq Z$，$\Psi(x)\subseteq F$ 意味着\emph{每个}中间选择 $y\in\Phi_1(x)$ 的全部后续输出都在 $F$，等价于 $\Phi_1(x)\subseteq\Phi_2^+(F)$。于是 $\Psi^+(F)=\Phi_1^+(\Phi_2^+(F))$。下半连续的闭集上逆像判据依次使内层、外层都闭，得到相同结论。该路线没有把复合对应当普通单值代入，而是明确保留了中间选择量词。
''')
put([57,58],r'''
沿用复合定义，但两对应现在上半连续。
\paragraph{开上逆像版本}任取开 $G\subseteq Z$。集合 $\Psi(x)=\bigcup_{y\in\Phi_1(x)}\Phi_2(y)$ 全在 $G$ 中，当且仅对每个 $y\in\Phi_1(x)$，$\Phi_2(y)\subseteq G$；也就是 $\Phi_1(x)\subseteq\Phi_2^+(G)$。所以
\[\Psi^+(G)=\Phi_1^+(\Phi_2^+(G)).\]
内层由 $\Phi_2$ 上半连续开，外层再由 $\Phi_1$ 上半连续开，故复合上半连续。
\paragraph{闭下逆像版本}对闭 $F$，展开存在量词得
\[x\in\Psi^-(F)\iff\exists y\in\Phi_1(x),\exists z\in\Phi_2(y)\cap F\iff x\in\Phi_1^-(\Phi_2^-(F)).\]
上半连续使闭集的下逆像闭，因此内层集合闭、外层逆像也闭，完成第二条原路线。注意同一个逆像恒等式在两类半连续性下应用的\emph{开闭条件}不同：本条用开上逆像及闭下逆像，不可混成下半连续的判据。
''')
put([59,60],r'''
设 $\Phi(x)=\bigcup_{\lambda\in\Lambda}\Phi_\lambda(x)$，各因子下半连续。对开 $G$，
\begin{align*}
x\in\Phi^-(G)&\iff\left(\bigcup_\lambda\Phi_\lambda(x)\right)\cap G\ne\varnothing\\
&\iff\exists\lambda,\ \Phi_\lambda(x)\cap G\ne\varnothing\\
&\iff x\in\bigcup_\lambda\Phi_\lambda^-(G).
\end{align*}
因此下逆像是开集的任意并，开，下半连续得证。这一等式的见证既包括输出点也包括因子编号，两个存在量词可以一起选，所以是真等式。
老师的闭集版本也要核查：对闭 $F$，全部并值在 $F$ 内当且仅每个因子值都在 $F$ 内，故 $\Phi^+(F)=\bigcap_\lambda\Phi_\lambda^+(F)$。各上逆像因下半连续而闭，任意闭交闭，再得结论。这里允许无限族，是因为第一种是任意开并，第二种是任意闭交，均不需要有限性。
''')
put([62],r'''
设各 $\Phi_\lambda$ 紧值上半连续。它们先有闭图，故交对应 $H(x)=\bigcap_\lambda\Phi_\lambda(x)$ 也有闭图。假设指标族非空，固定一个 $\lambda_0$。交值是闭集且包含于紧 $\Phi_{\lambda_0}(x)$，所以每个交值紧（可以为空）。
应用已经逐步证明的“闭图对应与紧值上半连续对应取交”定理：令闭图因子为 $H$，紧容器为 $\Phi_{\lambda_0}$。因 $H(x)\subseteq\Phi_{\lambda_0}(x)$，有 $H\cap\Phi_{\lambda_0}=H$，所以该定理给 $H$ 上半连续。
原页试图只从 $y\notin\bigcap_\lambda\Phi_\lambda(x)$ 推出它附近的闭图条件；这种逐点论证至多先证闭图，不能独自完成开集式上半连续。补上的紧容器步骤是原思路可成立的关键，不是可以忽略的技术细节。交值若要求非空，还要另外假设各值存在共同交，紧性本身不保证两个不交紧值会相交。
''')
# Retain and expand the typed diagnosis of the lecturer's invalid steps.
for ns,upper in [([67,68,69,70],True)]:
 put(ns,r'''
设有限 $\Phi(x)=\bigcup_{i=1}^m\Phi_i(x)$，各因子上半连续。第一组原页另有紧值条件，此时有限紧并也紧，下面先处理上半连续。
\paragraph{开上逆像的完整等价链}
\begin{align*}
x\in\Phi^+(G)&\iff\bigcup_i\Phi_i(x)\subseteq G\\
&\iff\forall i,\ \Phi_i(x)\subseteq G\\
&\iff x\in\bigcap_{i=1}^m\Phi_i^+(G).
\end{align*}
各因子对开 $G$ 的上逆像开，有限交仍开，所以并对应上半连续。有限性用在最后交的开性。
\paragraph{闭下逆像的原页另一种写法}
对闭 $F$，$\bigcup_i\Phi_i(x)$ 遇到 $F$ 等价于至少一个因子遇到 $F$，所以
\[\Phi^-(F)=\bigcup_{i=1}^m\Phi_i^-(F).\]
各因子对闭 $F$ 的下逆像闭，有限闭并仍闭，得到相同结论。原页若写成 $\Phi^-(F)=\bigcap_i\Phi_i^-(F)$ 则错误：有一个因子遇到 $F$ 不要求全部因子遇到它。若再假设紧值，任意开覆盖在每个紧因子上各取有限子覆盖，将有限多份有限集合合并，即给并值有限覆盖，故并值紧。
''')
put([71],r'''
令 $\Phi(x)=\prod_{i=1}^m\Phi_i(x)$。先对基本开矩形 $E=\prod_iG_i$，其中每个 $G_i$ 开，写出
\[\Phi(x)\cap E=\prod_i(\Phi_i(x)\cap G_i).\]
有限积非空当且仅每个因子非空，因此
\[\Phi^-(E)=\bigcap_{i=1}^m\Phi_i^-(G_i).\]
每个下逆像开，有限交开。
任意乘积空间开集 $G$ 都可写成基本开矩形的并 $G=\bigcup_kE_k$，指标不一定可数。于是
\begin{align*}
x\in\Phi^-(G)&\iff\exists y\in\Phi(x),\ y\in\bigcup_kE_k\\
&\iff\exists k,\exists y\in\Phi(x)\cap E_k\\
&\iff x\in\bigcup_k\Phi^-(E_k).
\end{align*}
因此下逆像为开集的任意并，开。老师第二条闭逆像路线可由开集取补对偶得到，不必把一般闭集错误地表示成闭矩形的交；后者表示并不一般成立。这一版本中基本开矩形的使用是合法的，因为是\emph{存在一点}落在并中。
''')
put([73],r'''
原课件两种证明均有需要明确指出的错误。先逐步重写其可用部分，再定位第一次失效的位置。
\paragraph{第一种原推导}对非空值的基本开矩形 $E=\prod_iG_i$，确有 $\Phi(x)\subseteq E\iff\forall i,\Phi_i(x)\subseteq G_i$，所以 $\Phi^+(E)=\bigcap_i\Phi_i^+(G_i)$ 开。接着把一般开集写成 $G=\bigcup_kE_k$，原页声称
\[\Phi^+(G)=\bigcup_k\Phi^+(E_k).\]
这一行不成立：一个值集整体落在许多矩形的并中，不要求整个值集落在其中某\emph{一个}矩形中。例值集 $\{0,1\}$ 被两个不交小开区间的并覆盖，却不在任何单个小区间内。故前面的基本矩形验证不足以直接得到一般开集结论。
\paragraph{第二种原推导}对基本闭矩形可得到有限交的下逆像公式，但原页随后假设任意闭集为闭矩形的交，这个表示本身一般不对；即使某个闭集确可如此写，仍不能使用
\[\Phi^-(\bigcap_kE_k)=\bigcap_k\Phi^-(E_k).\]
左边要求\emph{同一个}输出属于全部 $E_k$，右边允许为每个 $k$ 换一个输出。取 $\Phi(x)=\{0,1\},E_1=\{0\},E_2=\{1\}$，右边含 $x$，左边不含，直接否定等式。
因此两条写出的证明均未完成原结论。老师下一组原页75--76增加紧值并用有限覆盖，才提供可补严谨的路线。这里不把错误步骤删掉装成已证，而明确保留其论证位置和失效原因；要用于考试，应按紧值条件下下一条的完整证明。
''')
put([75],r'''
设 $K_1=\Phi_1(a),K_2=\Phi_2(a)$ 为紧值，且对应上半连续。先有积值紧：有限紧积的开覆盖证明可由两次有限覆盖得到，也可在有限维用闭性与有界性证明。要证上半连续，固定开 $G\supseteq K_1\times K_2$。原页希望构造开矩形 $V_1\times V_2$，使
\[K_1\times K_2\subseteq V_1\times V_2\subseteq G.\]
其投影交构造省略了最后包含的理由。下面仍沿原来的\emph{开矩形有限覆盖}路线补全这个关键引理。
\begin{enumerate}
\item 对固定 $y\in K_1$ 和每个 $z\in K_2$，乘积开性给矩形 $U_{y,z}\times W_{y,z}\subseteq G$ 含 $(y,z)$。$K_2$ 紧，选有限 $W_{y,z_j}$ 覆盖它。令 $U_y=\bigcap_jU_{y,z_j}$，$W_y=\bigcup_jW_{y,z_j}$。则 $U_y$ 开含 $y$，$W_y$ 开含整个 $K_2$，且 $U_y\times W_y\subseteq G$：任取第二坐标，选覆盖它的一个 $W_{y,z_j}$，第一坐标因在有限交中也在对应 $U_{y,z_j}$。
\item $\{U_y:y\in K_1\}$ 覆盖紧 $K_1$，选有限 $U_{y_1},\ldots,U_{y_r}$。令 $V_1=\bigcup_iU_{y_i}$，$V_2=\bigcap_iW_{y_i}$。它们开并分别含 $K_1,K_2$。若 $(u,v)\in V_1\times V_2$，选 $i$ 使 $u\in U_{y_i}$，则 $v\in W_{y_i}$，由第1步 $(u,v)\in G$。引理证毕。
\item 上半连续分别给输入邻域 $H_i$，使 $x\in H_i$ 时 $\Phi_i(x)\subseteq V_i$。取 $H=H_1\cap H_2$，则其中 $\Phi(x)\subseteq V_1\times V_2\subseteq G$，所以上半连续。
\end{enumerate}
若允许空值，在某个 $K_i$ 为空时，可对开空集使用该因子的上半连续性，附近该因子及积均空，结论也成立。有限多个因子由已证两因子结论归纳。这里保留的是老师需要的有限矩形控制，不用未经证明的投影等式跳过一般开集。
''')
put([78],r'''
设 $\Phi(x)=\sum_{i=1}^m\Phi_i(x)$，因子紧值上半连续。\textbf{先证紧值：}积 $\prod_i\Phi_i(x_0)$ 紧，加法映射 $F(y_1,\ldots,y_m)=\sum_iy_i$ 连续，其像正是和集 $K=\sum_i\Phi_i(x_0)$，所以 $K$ 紧。
\textbf{再按老师的零邻域法证上半连续。}给开 $G\supset K$，必须先找到0的开邻域 $V$ 使 $K+V\subset G$。对每个 $k\in K$，连续加法给邻域 $O_k\ni k,V_k\ni0$ 使 $O_k+V_k\subset G$。有限个 $O_{k_j}$ 覆盖紧 $K$，令 $V=\bigcap_jV_{k_j}$，则任取 $k\in K,v\in V$，选覆盖 $k$ 的 $O_{k_j}$，便得 $k+v\in G$。
加法在0连续，可为每个因子取0邻域 $W_i$，使 $\sum_iW_i\subseteq V$（欧氏空间中若 $B(0,r)\subset V$，可都取 $B(0,r/(2m))$）。上半连续给输入邻域 $U_i$，使 $\Phi_i(x)\subseteq\Phi_i(x_0)+W_i$ 对 $x\in U_i$ 成立。取有限交 $U$。其中任意和点 $y=\sum_iy_i$ 可写 $y_i=k_i+w_i$，于是
\[y=\sum_i k_i+\sum_iw_i\in K+\sum_iW_i\subseteq K+V\subset G.\]
所以 $\Phi(U)\subseteq G$，完成定义。原页把 $x\in\Phi_i(x_0)+V_i$ 写成输入属于输出集合，应修正为整个输出值集的包含；并把 $\sum_iW_i=V$ 修正成足够的包含关系。
''')
put([80],r'''
设 $H(x)=\operatorname{co}\Phi(x)$。给任意 $x_n\to x_0$ 和任意 $y_0\in H(x_0)$。凸包定义给\emph{有限}个旧值点 $z_1,\ldots,z_r\in\Phi(x_0)$ 与固定权重 $\lambda_i\ge0,\sum_i\lambda_i=1$，使 $y_0=\sum_i\lambda_i z_i$。
对每个 $i$，原对应下半连续的序列判据给 $z_{in}\in\Phi(x_n)$ 且 $z_{in}\to z_i$。令 $y_n=\sum_i\lambda_i z_{in}$。每个 $n$ 的权重仍非负且和1，所以 $y_n\in\operatorname{co}\Phi(x_n)=H(x_n)$；而
\[\|y_n-y_0\|\le\sum_{i=1}^r\lambda_i\|z_{in}-z_i\|\to0,\]
最后极限用有限项逐项收敛。于是任意旧凸包点都可沿任何输入列逼近，故 $H$ 下半连续。原页末尾 $y_n\in\Phi(x_0)$ 应改为 $y_n\in\operatorname{co}\Phi(x_n)$，因为它一般不是单个原值点，也不在旧输入的值集中。
''')
put([81],r'''
设输出在 $\R^L$，$\Phi$ 非空紧值上半连续。需要先补足老师未说明的\emph{统一有限点数}：Carathéodory 定理保证凸包每点可用至多 $L+1$ 个原点表示。理由是若一个表示有更多正权重点，增广向量 $(z_i,1)\in\R^{L+1}$ 线性相关，取不全零 $a_i$ 满足 $\sum_i a_iz_i=0,\sum_i a_i=0$，以 $t=\min_{a_i>0}\lambda_i/a_i$ 更新权重 $\lambda_i-ta_i$，保持总和及表示不变、保持非负并消去至少一项，有限次后剩至多 $L+1$ 项。
\paragraph{紧值}固定输入 $x$，凸包是紧单纯形 $\Delta^L$ 与紧集 $\Phi(x)^{L+1}$ 的积，在连续映射 $(\lambda,z)\mapsto\sum_i\lambda_i z_i$ 下的像，所以紧。
\paragraph{上半连续}取 $x_n\to x_0$，及任意 $y_n\in\operatorname{co}\Phi(x_n)$。写 $y_n=\sum_{i=1}^{L+1}\lambda_{in}z_{in}$；不足项以零权重补齐。权重在紧单纯形中，先抽子列使整组权重趋于 $\lambda_i$。再对有限个 $z_{in}\in\Phi(x_n)$ 逐次用紧值上半连续的选择紧性抽嵌套子列，最后每个 $z_{in}\to z_i\in\Phi(x_0)$，原已收敛权重仍保持极限。于是
\[y_n\to\sum_{i=1}^{L+1}\lambda_i z_i\in\operatorname{co}\Phi(x_0).\]
若上半连续不成立，选出逃离包含旧凸包值的开集的 $y_n$，上述收敛子列最终却应进入开集，矛盾。故结论成立。老师若让凸组合项数随 $n$ 任意变化而直接逐项抽子列，就缺了统一有限维表示这一必要步骤。
''')
put([85],r'''
在度量空间，证明下半连续等价于：每个 $x_n\to x_0$ 及每个 $y_0\in\Phi(x_0)$，均可选 $y_n\in\Phi(x_n)$ 使 $y_n\to y_0$。
\paragraph{序列性质推出下半连续：老师的反证方向}
若下半连续失败，有开 $G$ 遇到 $\Phi(x_0)$，却没有任何输入邻域保证附近值都遇到 $G$。选 $y_0\in\Phi(x_0)\cap G$。对每个 $n$，在球 $B(x_0,1/n)$ 内选 $x_n$ 使 $\Phi(x_n)\cap G=\varnothing$。此时 $x_n\to x_0$，序列性质却给 $y_n\in\Phi(x_n)$ 趋于 $y_0\in G$。开性使 $y_n$ 最终在 $G$ 中，违反空交。
\paragraph{下半连续推出序列性质：补足分段选点}
给 $x_n\to x_0,y_0\in\Phi(x_0)$。对每个精度编号 $j$，球 $V_j=B(y_0,1/j)$ 遇到旧值集，下半连续给 $x_0$ 邻域 $U_j$ 使 $\Phi(x)\cap V_j\ne\varnothing$ 对 $x\in U_j$ 成立。输入收敛给整数 $N_j$，使 $n\ge N_j$ 时 $x_n\in U_j$。把 $N_j$ 递增化，例如递归改成 $\max(N_j,N_{j-1}+1,j)$，不破坏性质。
当 $N_j\le n<N_{j+1}$ 时，在非空交 $\Phi(x_n)\cap V_j$ 选 $y_n$；初始有限项在非空值中任取。若 $n\to\infty$，其所处分段编号 $j\to\infty$，而 $\|y_n-y_0\|<1/j$。因此给任意 $\eps$，选 $j_0$ 使 $1/j_0<\eps$，所有 $n\ge N_{j_0}$ 都满足误差界。故所选整列收敛，而非仅有某条子列。
''')
put([87],r'''
本页 o.s.c. 采用较强序列定义：任意 $x_n\to x_0,y_n\in\Phi(x_n)$，都能抽输出收敛子列，且其极限属于旧值集。它同时含“不逃向无穷”与“已有极限不漏出”两个要求，不能与仅闭图的常见外半连续定义混淆。
\paragraph{紧值上半连续给可抽子列}
集合 $K=\{x_0,x_1,x_2,\ldots\}$ 紧：任意开覆盖中选含 $x_0$ 的一个开集，输入收敛使它覆盖全部足够晚的 $x_n$，余下有限点各选一个成员即可。紧值上半连续的紧像定理使 $\Phi(K)$ 紧。全部 $y_n$ 在该紧像中，度量紧性给子列 $y_{n_k}\to y_0$。注意紧像只能先给极限在整个像中，尚不能宣布 $y_0\in\Phi(x_0)$。
\paragraph{原页88的距离分离法}
若 $y_0\notin\Phi(x_0)$，旧值集闭使 $d=\operatorname{dist}(y_0,\Phi(x_0))>0$。上半连续对旧值的 $d/3$ 开邻域给输入邻域，使足够晚的 $y_{n_k}$ 距旧值小于 $d/3$。输出收敛同时使其距 $y_0$ 小于 $d/3$，两段相加便给 $d<2d/3$，矛盾。因此极限在旧值。
\paragraph{原页89的不交邻域法}
也可选不交开集 $V\supseteq\Phi(x_0)$ 与 $W\ni y_0$；紧旧值与外点可如此分离。上半连续使子列输出最终在 $V$，收敛使其最终在 $W$，同时满足便落入空交，矛盾。两种方法分别展开，而不是省略为“显然闭图”。
''')
put([90,91],r'''
假设本课强序列性质成立。要证上半连续，固定 $x_0$ 及开 $G\supseteq\Phi(x_0)$。反设不存在邻域 $U$ 使附近值全在 $G$。于是对每个 $n$ 都能选 $x_n\in B(x_0,1/n)$ 及 $y_n\in\Phi(x_n)\setminus G$。这里必须先选输入，再从“值集不包含于 $G$”选出一个逃出的输出。
输入列趋于 $x_0$，强序列性质给子列 $y_{n_k}\to y_0\in\Phi(x_0)$。因 $G$ 开且含 $y_0$，存在球 $B(y_0,r)\subseteq G$，子列最终在这个球中，因此最终在 $G$。但其每项按选择都不在 $G$，矛盾，所以上半连续。
等价地，原页另一版本可先指出 $Y\setminus G$ 闭，逃出子列的极限必须仍在这个补集中，却又属于 $\Phi(x_0)\subset G$。两种写法使用的是同一闭/开极限事实，并不需要假设原整列 $y_n$ 收敛。只有子列收敛已足够制造矛盾。
''')
put([92],r'''
设 $\Psi=\Phi_2\circ\Phi_1$，两因子内半连续。给任意 $x_n\to x_0$ 及任意 $z_0\in\Psi(x_0)$。复合归属定义保证\emph{存在一个} $y_0\in\Phi_1(x_0)$，使 $z_0\in\Phi_2(y_0)$。
先用第一个对应内半连续，为给定整条输入列选 $y_n\in\Phi_1(x_n)$ 且 $y_n\to y_0$。再把这一整条 $y_n$ 当作第二对应的输入列，并把 $z_0\in\Phi_2(y_0)$ 当旧输出，用第二个对应内半连续选 $z_n\in\Phi_2(y_n)$ 且 $z_n\to z_0$。
由于每个 $y_n\in\Phi_1(x_n)$，复合的并值定义给 $\Phi_2(y_n)\subseteq\Psi(x_n)$，所以每个 $z_n\in\Psi(x_n)$。这条整列趋于给定 $z_0$，正是复合内半连续。不要把中间存在点 $y_0$ 当成唯一，也不要求选择函数在全域连续。
''')
put([93],r'''
采用本课强 o.s.c. 定义。给任意 $x_n\to x_0$ 和 $z_n\in(\Phi_2\circ\Phi_1)(x_n)$，逐项选 $y_n\in\Phi_1(x_n)$ 使 $z_n\in\Phi_2(y_n)$。这些中间选择一般不唯一，任取一组即可。
第一对应的强性质给严格递增 $n_k$，使 $y_{n_k}\to y_0\in\Phi_1(x_0)$。现在必须把第二对应的输入、输出\emph{一起限制}到同一个子列：$z_{n_k}\in\Phi_2(y_{n_k})$。第二对应的强性质再给严格递增 $k_j$，使 $z_{n_{k_j}}\to z_0\in\Phi_2(y_0)$。已经选好的 $y$ 子列在再次抽子列后仍趋于 $y_0$。
因为 $y_0\in\Phi_1(x_0)$，有 $\Phi_2(y_0)\subseteq(\Phi_2\circ\Phi_1)(x_0)$，故输出极限在复合旧值中。于是对任意选择列都有所需收敛子列，完成定义。不能分别独立抽两个子列后擅自认为下标一致，老师的两次嵌套正是为此。
''')
put([94],r'''
设 $\Phi(x)=\prod_{i=1}^m\Phi_i(x)$，因子内半连续。给 $x_n\to x_0$ 及旧积值 $y_0=(y_{10},\ldots,y_{m0})\in\Phi(x_0)$，则每个 $y_{i0}\in\Phi_i(x_0)$。
对每个固定 $i$，内半连续给整列 $y_{in}\in\Phi_i(x_n)$ 趋于 $y_{i0}$。定义 $y_n=(y_{1n},\ldots,y_{mn})$，逐坐标归属使 $y_n\in\Phi(x_n)$。且
\[\|y_n-y_0\|^2=\sum_{i=1}^m\|y_{in}-y_{i0}\|^2\to0,\]
因为只有有限个趋零项。所以完整选择列趋于旧积值，积对应内半连续。这里不需要抽子列：每个因子都能沿同一给定整列输入逼近，直接组合即可。
''')
put([95],r'''
给 $x_n\to x_0$，输出 $y_n=(y_{1n},\ldots,y_{mn})\in\prod_i\Phi_i(x_n)$。由第一因子的强性质，抽指标子列 $n^{(1)}_k$ 使第一坐标收敛到旧第一值中的点。将输入与所有其余坐标\emph{同时}限制到这些指标。第二因子再从该子列抽 $n^{(2)}_k$ 使第二坐标收敛，而第一坐标已收敛所以新子列仍保其极限。
重复有限 $m$ 次。最终一组指标是前面每组的子列，故所有坐标都收敛，且各极限 $y_{i0}\in\Phi_i(x_0)$。有限维坐标收敛合成 $y_n\to y_0=(y_{10},\ldots,y_{m0})\in\prod_i\Phi_i(x_0)$。这就完成积的强序列性质。
不能一开始对每个坐标独立抽子列再拼接，因为不同坐标可能得到不相容的指标。有限次嵌套是原证明的实际逻辑；无穷次嵌套需要另外的对角构造，本条没有用到。
''')
put([96],r'''
令 $M(x)=\sup_{y\in\Phi(x)} f(x,y)$，假定讨论的 $M(x_0)$ 有限，$\Phi$ 非空值下半连续，$f$ 联合下半连续。老师要通过一个近似最优旧选择建立附近最优值的下界。
\begin{enumerate}
\item 任给 $\eps>0$。由上确界逼近，选 $y_0\in\Phi(x_0)$ 满足 $f(x_0,y_0)>M(x_0)-\eps/2$。不要求真最优点存在，不能把 $\sup$ 未经证明换成 $\max$。
\item 目标在 $(x_0,y_0)$ 下半连续，故存在乘积邻域 $U_1\times V$，使其中每点满足 $f(x,y)>f(x_0,y_0)-\eps/2$。这样在此邻域内有 $f(x,y)>M(x_0)-\eps$。
\item 因 $y_0\in\Phi(x_0)\cap V$ 且 $V$ 开，可行对应下半连续给 $U_2$，使 $\Phi(x)\cap V\ne\varnothing$ 对 $x\in U_2$ 成立。
\item 对任意 $x\in U_1\cap U_2$，从该交选一个 $y_x$。它可行且位于目标控制邻域，所以
\[M(x)\ge f(x,y_x)>f(x_0,y_0)-\eps/2>M(x_0)-\eps.\]
\end{enumerate}
每个精度都有这样的输入邻域，故 $M$ 下半连续。证明只需要一个好的附近可行点，不要求控制全部可行点；这也解释为何可行对应使用下半连续。
''')
put([98],E['108:98']+r'''
进一步核查有限覆盖中每个选择的先后：先固定 $x_0,\eps$，再对每个旧可行点 $y$ 取联合目标邻域；紧性选择有限个之后，才取输入邻域的交。若一开始对所有 $y$ 的输入邻域作无限交，这个交未必仍是邻域，证明会失效。
最大值存在也需解释：固定 $x$ 时，$f(x,\cdot)$ 为上半连续实值函数，非空紧可行集上取最大值；其有上界及达到上确界可由闭上水平集的有限交性质证明。因此这里 $M(x)$ 确实是一个达到的有限数，而不是未经控制的无穷上确界。
''')
_max=r'''
设 $\Phi$ 非空紧值连续，$f$ 联合连续。分别定义最优值与最优点对应：
\[g(x)=\max_{y\in\Phi(x)}f(x,y),\qquad M(x)=\{y\in\Phi(x):f(x,y)=g(x)\}.\]
\begin{enumerate}
\item 固定输入后目标连续且可行集非空紧，极值定理保证 $g$ 有限且 $M(x)$ 非空。等值集合闭，与紧可行值相交使 $M(x)$ 紧。
\item 因 $f$ 连续同时上、下半连续，$\Phi$ 连续也同时上、下半连续，前两条最优值估计分别给 $g$ 下半连续与上半连续，所以 $g$ 连续。要把两种局部估计合成一次误差控制，取两输入邻域的交即可。
\item 令 $\Delta(x)=\{y:f(x,y)\ge g(x)\}$。函数 $(x,y)\mapsto g(x)-f(x,y)$ 连续，弱子水平定义使 $\Delta$ 有闭图：对图内收敛序列取极限保弱不等式。
\item 由最大值定义，每个 $y\in\Phi(x)$ 都有 $f(x,y)\le g(x)$。因此在可行集内再要求 $f(x,y)\ge g(x)$，恰好强迫等号，故 $M=\Phi\cap\Delta$。
\item 闭图 $\Delta$ 与紧值上半连续容器 $\Phi$ 的交定理给 $M$ 上半连续。这里是该交定理的明确应用，不能只说“最优点集合闭所以连续”；逐点闭值远弱于上半连续。
\end{enumerate}
若原页目标只依赖 $y$，将 $f(x,y)$ 理解为不随输入变化的函数即可。非空紧值是假设中的实质条件，原页省略它时必须补明；例如可行集 $(0,1)$ 上目标 $f(y)=y$ 连最大点都不存在。
'''
put([99],_max)
put([101,102],r'''
老师假定有一个\emph{共同}的连续实值目标 $f$，每个非空紧可行集 $\Phi(x)$ 上恰有一个最大点。写 $M(x)=\{\sigma(x)\}$。最大值定理给最优对应 $M$ 上半连续。
要将单点对应上半连续变成普通函数连续，固定 $x_0$ 和任意含 $\sigma(x_0)$ 的开集 $G$。因 $M(x_0)=\{\sigma(x_0)\}\subseteq G$，上半连续给输入邻域 $U$ 使 $M(x)\subseteq G$ 对 $x\in U$。单点归属等价于 $\sigma(x)\in G$，这正是函数的邻域连续定义。又最优点本来在可行集中，所以 $\sigma(x)\in\Phi(x)$，得到连续选择。
实数值域的推论取共同目标 $f(y)=y$。任意非空紧实数集均达到最大值，而且作为\emph{实数元素}的最大者唯一，即使集合有许多其他点。因此 $\sigma(x)=\max\Phi(x)$ 是连续选择。这里不是说每个连续对应都天然有唯一最优点，而是先找到一个使这些值集都具有唯一最优点的共同目标；实数顺序使这一步特别容易。
''')
put([103],r'''
设 $m(x)=\inf_{y\in\Phi(x)}f(x,y)$，$f$ 联合下半连续，$\Phi$ 非空紧值上半连续。固定输入后的极值定理使下确界有限并达到。
给 $x_0,\eps>0$。对每个 $y\in\Phi(x_0)$，目标下半连续给乘积邻域 $U_y\times V_y$，其中
\[f(x,z)>f(x_0,y)-\eps\ge m(x_0)-\eps.\]
紧旧值被有限 $V_{y_1},\ldots,V_{y_r}$ 覆盖。上半连续给 $U_0$ 使附近全部可行值在它们的并中；取 $U=U_0\cap\bigcap_{i=1}^rU_{y_i}$。任意 $x\in U,z\in\Phi(x)$，选覆盖 $z$ 的 $V_{y_i}$，对应输入条件也成立，所以 $f(x,z)>m(x_0)-\eps$。对全部可行 $z$ 取下确界，得
\[m(x)\ge m(x_0)-\eps.\]
若需要定义中的严格界，证明开始以 $\eps/2$ 代替 $\eps$，最后便有 $m(x)>m(x_0)-\eps$。所以下半连续。
原课件末尾把结果 $m(x)$ 写成 $m(x_0)$，应修正；真正需要比较的是\emph{附近输入的最小值}。有限覆盖先于取输入交，保证所取交仍是邻域。
''')
put([105],r'''
设 $m(x)=\inf_{y\in\Phi(x)}f(x,y)$，讨论实值情形。$f$ 联合上半连续，$\Phi$ 非空值下半连续。给定 $x_0,\eps>0$，下确界性质给旧可行点 $y_0$ 使 $f(x_0,y_0)<m(x_0)+\eps/2$；不必真达到最小值。
目标上半连续给乘积邻域 $U_1\times V$，其中 $f(x,y)<f(x_0,y_0)+\eps/2<m(x_0)+\eps$。因旧值遇到 $V$，可行下半连续给 $U_2$，使每个 $x\in U_2$ 至少有一个 $y_x\in\Phi(x)\cap V$。对 $x\in U_1\cap U_2$，
\[m(x)\le f(x,y_x)<m(x_0)+\eps.\]
所以 $m$ 上半连续。这里 $y_x$ 可随输入改变，只需一个合法的好选择，故用下半连续而非要求所有附近选择保持小。
原页 $\Phi(x)\subseteq\Phi(x)\cap V\ne\varnothing$ 错误：下半连续只保证交非空，不保证全部值落在 $V$ 内。将它改成上述选点，老师后续不等式才有正确依据。
''')
put([107],r'''
设 $f$ 连续、$\Phi$ 非空紧值连续，$m(x)=\min_{y\in\Phi(x)}f(x,y)$。紧性和连续性先保证有限最小值及非空最小点集。前条两种最小值估计使 $m$ 同时上下半连续，故连续。
令 $\Delta(x)=\{y:f(x,y)\le m(x)\}$。因 $f-m$ 连续，$\Delta$ 图闭。可行点均满足 $f(x,y)\ge m(x)$，所以在 $\Phi(x)$ 内附加弱反向不等式恰等于要求等号。因此最小对应
\[M(x)=\{y\in\Phi(x):f(x,y)=m(x)\}=\Phi(x)\cap\Delta(x).\]
闭图与紧上半连续容器相交给上半连续，交值也是紧集闭子集，故紧。
原页若写 $m(x)-f(y)\le0$，该条件就是 $m(x)\le f(y)$，对每个可行点都已成立，会把全部可行集误当最优集。正确的附加方向应为 $f(y)-m(x)\le0$，或者直接用等式避免混淆。这里修正的仅是不等式方向，整体仍沿老师“连续值函数—闭约束对应—与可行对应取交”的路线。
''')
put([110],r'''
设 $\beta$ 非空紧值连续，每个严格关系 $\prec_x$ 传递且非自反，且可行三元组中“不满足 $y\prec_x z$”的集合闭。定义 $M(x)$ 为不被任何可行 $z$ 严格压过的点。
\paragraph{第一步：固定输入证明极大元存在}
反设某个 $x$ 没有极大元。于是每个 $y\in\beta(x)$ 都被某个 $z\in\beta(x)$ 压过。令 $R_z=\{y\in\beta(x):y\prec_x z\}$。非优关系的闭性使严格下截集在可行值中相对开，且这些 $R_z$ 覆盖 $\beta(x)$。紧性给有限覆盖 $R_{z_1},\ldots,R_{z_r}$。
有限集 $\{z_1,\ldots,z_r\}$ 中必有极大者 $z_j$：从任一点若非极大就移到一个严格更优点，若一直没有停下，有限性使重复出现某点，传递性便得到该点严格优于自己，违反非自反。因此过程有限步停下。
由 $z_j$ 在有限集极大，$z_j$ 不在任何 $R_{z_i}$；包括 $i=j$ 也由非自反排除。但 $z_j\in\beta(x)$，与这些 $R_{z_i}$ 覆盖矛盾。故极大元非空。
\paragraph{第二步：固定输入证明紧值}
\[M(x)=\bigcap_{z\in\beta(x)}\{y\in\beta(x):\neg(y\prec_x z)\}.\]
每项由非优关系闭性为相对闭集，任意交仍闭；它是紧 $\beta(x)$ 的闭子集，故紧。
\paragraph{第三步：证明最优图闭}
设 $x_n\to x,y_n\to y,y_n\in M(x_n)$。$\beta$ 紧值上半连续给闭图，故 $y\in\beta(x)$。任取竞争点 $z\in\beta(x)$，$\beta$ 下半连续给 $z_n\in\beta(x_n)$ 且 $z_n\to z$。因为 $y_n$ 极大，$\neg(y_n\prec_{x_n}z_n)$ 对所有 $n$ 成立。对可行三元组取极限，非优关系的闭性给 $\neg(y\prec_x z)$。$z$ 任意，所以 $y\in M(x)$。
\paragraph{第四步：由紧容器得到上半连续}
$M$ 图闭且逐点包含于紧值上半连续 $\beta$，所以 $M=M\cap\beta$，交对应定理给上半连续。原页说只要闭值即足够不准确，第三步实际证明的是闭\emph{图}。原页 $z_n\in M(x_n)$ 应为 $z_n\in\beta(x_n)$，因为我们逼近的是任意竞争者，不要求它也最优。
''')
put([113],r'''
给定连续实值目标 $f(x,y)$，定义 $y\prec_x z\iff f(x,y)<f(x,z)$。实数严格大小关系传递且非自反，因此这些关系满足极大元定理的代数条件。非优三元组由 $f(x,y)-f(x,z)\ge0$ 刻画，是连续函数的弱水平集，在可行三元组中闭。于是前条给非空紧最优对应 $M$ 上半连续。
老师还希望从最优对应推回最优值连续。令 $H(x)=\{x\}\times M(x)$；输入单点对应连续，有限紧值上半连续积定理给 $H$ 上半连续且紧值。连续函数 $(x,y)\mapsto f(x,y)$ 将该对应复合为输出对应
\[V(x)=\{f(x,y):y\in M(x)\}.\]
因为每个最优点的目标值都相同，$V(x)=\{g(x)\}$ 为\emph{单点值}。连续函数可看作单点值连续对应，与 $H$ 复合仍上半连续。对单点值对应，上半连续等价于普通函数连续：给含 $g(x_0)$ 的开邻域，上半连续直接保证附近 $g(x)$ 仍在其中。故 $g$ 连续。
这里不能把 $M$ 自身称为单点值，它可以有多个最优点；单点的是其\emph{目标值像}。原页把最优对应与目标函数都记作 $f$ 时容易混乱，故这里用 $M,V,g$ 分开写出全部对象。
''')
