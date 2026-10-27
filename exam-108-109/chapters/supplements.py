SUPPLEMENTS={}
SUPPLEMENTS[('108',47)]=r'''
\paragraph{把第48--49页最后一串包含再拆开。}
给 $x\in U_1\cap U_2$，任取 $z\in H(x)$。由 $z\in\Phi_2(x)$ 知 $z\in G\cup V$，因此只有“在 $G$ 中”或“在 $V$ 中”两种可能。由 $z\in\Phi_1(x)$ 和 $\Phi_1(U_1)\cap V=\varnothing$ 知 $z\notin V$，剩下只能 $z\in G$。因为 $z$ 任意，得到 $H(x)\subseteq G$；因为 $x$ 任意，得到同一邻域内全部值都在 $G$。这才完整匹配上半连续定义中的两个全称量词。
为什么 $\Phi_1(U_1)$ 避开\emph{整个} $V$？若它碰到 $V=\bigcup_i V_{y_i}$，就碰到某个 $V_{y_i}$；而 $U_1\subseteq U_{y_i}$ 使 $\Phi_1(U_1)\subseteq\Phi_1(U_{y_i})$，与该因子的空交矛盾。有限性同时保证 $U_1$ 仍是邻域，这不是单纯的集合运算装饰。
'''
SUPPLEMENTS[('108',81)]=r'''
\paragraph{Carathéodory 补步中，为什么更新权重不会变负？}
先删去所有零权重，故当前 $\lambda_i>0$。依赖系数 $a_i$ 不全零且和为0，故同时有正项与负项。取 $t=\min_{a_i>0}\lambda_i/a_i>0$。若 $a_i>0$，则 $t\le\lambda_i/a_i$，所以 $\lambda_i-ta_i\ge0$；若 $a_i\le0$，新权重不小于原来的正权重。至少一个达到最小比值的指标使新权重为0，可以删去。同时
\[\sum_i(\lambda_i-ta_i)=1-t\cdot0=1,
\quad \sum_i(\lambda_i-ta_i)z_i=\sum_i\lambda_i z_i-t\cdot0=y.
\]
所以表示的点没有变，合法性没有变，正权重项数减少。重复这个有限过程即可得到至多 $L+1$ 项。统一的 $L+1$ 是由\emph{输出维数}决定的，和输入序列编号无关。
'''
SUPPLEMENTS[('108',83)]=r'''
\paragraph{补充：怎样实际构造闭包仍在 $G$ 内的开集？}
令 $A=\overline{\Phi(x_0)}$、$B=T\setminus G$，它们不交且闭。若 $A$ 或 $B$ 为空可直接处理；否则距离函数连续，取
\[V=\{z:\dist(z,A)<\tfrac13\dist(z,B)\}.
\]
对 $a\in A$，距离 $\dist(a,A)=0$，而 $B$ 闭且不含 $a$ 使 $\dist(a,B)>0$，故 $a\in V$。不等号严格使 $V$ 开。若 $z\in\overline V$，连续性给 $\dist(z,A)\le\tfrac13\dist(z,B)$。若还 $z\in B$，右边0，便得 $\dist(z,A)=0$，闭性使 $z\in A$，与不交矛盾。所以 $\overline V\subseteq T\setminus B=G$。这把正文的度量空间分离性质具体实现出来。
'''
SUPPLEMENTS[('109',63)]=r'''
\subsection*{补充证明：原页63的 Minkowski 定理}
以下 $N\ge1$。要证的是存在 $p\ne0$，使 $p\cdot(z-x)\le0$ 对全部 $z\in K$ 成立；相应经过 $x$ 的平面是 $p\cdot(z-x)=0$。这把几何目标翻译成了一个可验证的不等式。

\paragraph{第一步：有平面则不能是内点。}
若 $x$ 是内点，就有球 $N(x,r)\subseteq K$。取 $z=x+(r/2)p/\|p\|$，它在这个球内，故在 $K$，但
\[p\cdot(z-x)=(r/2)\|p\|>0,
\]
与所有点都满足非正不等式矛盾。若原来在另一侧，把法向量变为 $-p$ 即可，因此必要性完成。

\paragraph{第二步：闭凸集外一点的最近点存在。}
暂设 $C$ 非空闭凸、$q\notin C$。取 $a\in C$，设 $R=\|q-a\|$。为了寻找最小距离，只需在 $C\cap\overline B(q,R)$ 中找：球外点比已知候选 $a$ 更远。这个交非空闭有界，所以紧；连续函数 $z\mapsto\|q-z\|$ 在其上达到最小值，记最近点为 $b$。因此它也是整个 $C$ 上的最近点。$q\notin C$ 保证 $q\ne b$。

任取 $z\in C$ 和 $0<t\le1$，凸性给 $b+t(z-b)\in C$，最近性给
\begin{align*}
\|q-b\|^2&\le\|q-b-t(z-b)\|^2\\
&=\|q-b\|^2-2t(q-b)\cdot(z-b)+t^2\|z-b\|^2.
\end{align*}
减去共同项并除以正数 $t$，得 $2(q-b)\cdot(z-b)\le t\|z-b\|^2$。让 $t\downarrow0$，得到
\[(q-b)\cdot(z-b)\le0\quad(z\in C).\tag{*}
\]
所以令 $p=q-b$，又有
\[p\cdot(z-q)=p\cdot(z-b)-\|p\|^2\le-\|p\|^2<0.
\]
这说明\emph{经过外点 $q$} 的平面也能界住 $C$。

\paragraph{第三步：闭凸集边界点的支撑平面。}
设 $x\in C\setminus\Int C$。它的每个邻域都含 $C$ 外点，可选 $q_n\notin C$ 且 $\|q_n-x\|<1/n$。为每个 $q_n$ 取最近点 $b_n\in C$。因 $x$ 本身是候选，
\[\|q_n-b_n\|\le\|q_n-x\|,
\quad\|b_n-x\|\le\|b_n-q_n\|+\|q_n-x\|<2/n.
\]
故 $b_n\to x$。把非零法向量归一化为 $p_n=(q_n-b_n)/\|q_n-b_n\|$，单位球面紧，抽子列 $p_{n_k}\to p$，且 $\|p\|=1$。将 $(*)$ 除以正的范数，得到 $p_{n_k}\cdot(z-b_{n_k})\le0$。对\emph{固定任意} $z\in C$ 取极限，内积连续给 $p\cdot(z-x)\le0$。$p\ne0$，即所需平面。这里不需要给每个 $z$ 重抽子列：子列早已只由 $p_n$ 选定。

\paragraph{第四步：原命题没要求 $K$ 闭，需要补这个环节。}
令 $C=\overline K$，它闭凸。我们需要保证 $x\notin\Int K$ 时也 $x\notin\Int C$。对凸集确有
\[\Int\overline K=\Int K.\tag{**}
\]
一边由 $K\subseteq\overline K$ 直接成立。证明另一边，取 $x\in\Int\overline K$，选球 $N(x,r)\subseteq\overline K$。取很小 $a>0$，使下面 $N+1$ 个点全在球中：
\[v_0=x-a\sum_{j=1}^Ne_j,\qquad v_i=x+ae_i\quad(1\le i\le N).
\]
这些点仿射独立，并且 $x=(v_0+\cdots+v_N)/(N+1)$，所有权重严格正。因此 $x$ 在该单纯形内部。每个 $v_i\in\overline K$，可选 $z_i\in K$ 任意接近 $v_i$；足够接近时仍仿射独立，且表示 $x$ 的重心坐标仍严格正。这个“仍”可由线性方程检查：把增广列 $(z_i,1)$ 组成方阵，其行列式在 $v_i$ 处非零，故小扰动下仍非零；解 $\sum_i\lambda_i z_i=x,\sum_i\lambda_i=1$ 由逆矩阵连续依赖各 $z_i$，因此各 $\lambda_i$ 仍接近正数 $1/(N+1)$。进一步把 $x$ 小幅移动时，权重也仍为正，所以 $x$ 的一个小球包含于 $\conv\{z_0,\ldots,z_N\}$。凸性使这个凸包包含于 $K$，故 $x\in\Int K$，证明 $(**)$。

现在 $x\notin\Int C$：若 $x\notin C$，用第二步；若 $x\in C$，用第三步。得到界住 $C$ 的平面，自然也界住 $K\subseteq C$。若 $K=\varnothing$，任意经过 $x$ 的超平面都符合条件，单独成立。充分性完成。

\paragraph{考试如何定位这份补充。}
课件原页只有定理陈述，以上最近点、单位法向量子列与凸集内部引理是自足补充。若老师只要求引用本定理，可直接写准确条件与结论；若要求证明，则不能把非闭凸集情况默默当作闭集。
'''
