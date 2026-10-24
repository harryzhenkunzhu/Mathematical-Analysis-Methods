# Mathematical Analysis Methods｜数理分析方法

本仓库用于整理张顺明教授数理分析方法课程的**12 份逐页自学 LaTeX 讲义**。课程材料以教师 PPT 为主，Debreu (1959) *Theory of Value* 仅作参考，不另立笔记。

## 课程目录

| 源 PPT | 主题 | 原始页数 |
|---|---|---:|
| 000-PPT | 数理经济学与均衡存在性概览 | 19 |
| 000-ZSM-PPT | 实数理论基础定理 | 62 |
| 101-ZSM-PPT | 数学基础导论 | 10 |
| 102-ZSM-PPT | 集合论 | 53 |
| 103-ZSM-PPT | 函数与对应 | 35 |
| 104-ZSM-PPT | 预序与偏好 | 29 |
| 105-ZSM-PPT | 实数与完备性 | 67 |
| 106-ZSM-PPT | 极限、开闭集和紧致性 | 100 |
| 107-ZSM-PPT | 连续函数 | 43 |
| 108-ZSM-PPT | 连续对应与最大值定理 | 113 |
| 109-ZSM-PPT | 向量、凸性、渐近锥 | 118 |
| 110-ZSM-PPT | Brouwer 与 Kakutani 不动点 | 8 |

**总计 657 页原始教师课件。** 编写原则：逐页对应、保留原课件画面、中文解释、重视证明步骤、补充基础数学知识。

## 讲义使用与编译

本仓库的 LaTeX 索引模板位于 `tex/`。需要将对应的原始 PPT PDF 放进 `slides/`，然后安装 TeX Live / MacTeX，用 XeLaTeX 编译。例如：

```bash
cd tex
xelatex 110-ZSM-PPT.tex
```

**目前 GitHub 版本是课程结构和逐页编译入口；完整讲解、证明专题和已编译 PDF 另以本次 ChatGPT 会话中的下载压缩包交付。** 因受限于 GitHub 连接器的二进制文件传输接口，完整 PDF 与课件文件尚未全部直接进入此仓库。不要误将仓库中的模板视为与本地压缩包完全相同的完整版。

## 特别关注的严谨性问题

- 闭区间套、最小上界、柯西收敛准则与实数完备性的相互联系
- 集合恒等式、函数像与逆像的区别
- 上半连续与下半连续、Berge 最大值定理
- 凸集、分离超平面与渐近锥
- Brouwer/Kakutani 适用条件；不能笼统声称任意紧凸集都与同维闭球同胚

参考教材：Gérard Debreu, *Theory of Value: An Axiomatic Analysis of Economic Equilibrium* (1959)。原始教材扫描件不在本仓库重新发布。
