# 数理分析方法：中文自学 Lecture Notes

新增：[老师实际证明过程合并 PDF](pdf/gpt-All-Proofs.pdf) · [证明汇编说明及页码索引](proofs/README.md) · [证明汇编 ZIP 下载](downloads/gpt-Proofs-complete.zip)

每份课件对应一本独立 PDF。**原课件全部 657 页逐页嵌入**，其后附中文讲解；相关证明按主题集中展开，后续展开页给出具体原页索引。两份 `000` 是不同课件，因此分别保留为 `gpt-000` 与 `gpt-000-ZSM`。

为没有数学分析基础的读者，所有讲义附量词、集合证明、数列和误差估计的入门说明。讲解区分原课件、补充证明、必要条件与笔误修正。人物介绍和目录页按原有用途解释；数学页重点补全证明逻辑，并用反例区分容易混淆的条件。

## 阅读与下载

| 编号 | 内容 | 原课件页数 | 已编译讲义 | LaTeX 入口 |
|---|---|---:|---|---|
| 000 | 课程导论与证明入门 | 19 | [gpt-000.pdf](pdf/gpt-000.pdf) | [000.tex](notes/000.tex) |
| 000-ZSM | 实数基础与完备性 | 62 | [gpt-000-ZSM.pdf](pdf/gpt-000-ZSM.pdf) | [000-ZSM.tex](notes/000-ZSM.tex) |
| 101 | 数学语言与公理方法 | 10 | [gpt-101.pdf](pdf/gpt-101.pdf) | [101.tex](notes/101.tex) |
| 102 | 集合与集合运算 | 53 | [gpt-102.pdf](pdf/gpt-102.pdf) | [102.tex](notes/102.tex) |
| 103 | 函数、对应与可数集 | 35 | [gpt-103.pdf](pdf/gpt-103.pdf) | [103.tex](notes/103.tex) |
| 104 | 关系、预序与偏好 | 29 | [gpt-104.pdf](pdf/gpt-104.pdf) | [104.tex](notes/104.tex) |
| 105 | 实数与基本定理 | 67 | [gpt-105.pdf](pdf/gpt-105.pdf) | [105.tex](notes/105.tex) |
| 106 | 欧氏空间的极限与拓扑 | 100 | [gpt-106.pdf](pdf/gpt-106.pdf) | [106.tex](notes/106.tex) |
| 107 | 连续函数 | 43 | [gpt-107.pdf](pdf/gpt-107.pdf) | [107.tex](notes/107.tex) |
| 108 | 连续对应与最优化 | 113 | [gpt-108.pdf](pdf/gpt-108.pdf) | [108.tex](notes/108.tex) |
| 109 | 向量、凸性与渐近锥 | 118 | [gpt-109.pdf](pdf/gpt-109.pdf) | [109.tex](notes/109.tex) |
| 110 | 不动点定理 | 8 | [gpt-110.pdf](pdf/gpt-110.pdf) | [110.tex](notes/110.tex) |

建议先读 `000` 的课程定位，实数基础遇到困难时先学 `102–104` 的语言，再读 `000-ZSM/105`，然后依次学习 `106–110`。`000-ZSM` 与 `105` 有大量相同的实数基础材料，两本仍各自保留所有原页，不删重复页。

## 证明复习方法

每读完一个命题，遮住证明，先写“假设—目标—构造—理由—结论”。重点掌握：逐元素法、双向包含、逆否与反证、确界逼近、二分区间、子列抽取、有限子覆盖、分离超平面，以及不动点的逼近构造。不要只背定理名称，也不要把存在性误记为唯一性。

特别说明：课件中存在若干需要修正的表述，例如一般紧凸集不必与同维闭球同胚、最大值定理须保证非空紧值、下半连续对应的交不一定下半连续。正文保留原图并明确解释这些问题。110 补充 Sperner 引理到 Brouwer 的证明，以及由 Brouwer 推导 Kakutani 的近似选择论证。

## 材料与参考对应

原页来自用户提供的张顺明教授课程 PDF，保存在 `sources/`。直接嵌入 PDF 原页以保留矢量公式与图形，等价于清晰截图，不依赖外部网络资源。

参考 Gérard Debreu, *Theory of Value: An Axiomatic Analysis of Economic Equilibrium* (1959)，第一章 *Mathematics*：101 对应 §1.1；102 对应 §1.2；103 对应 §1.3；104 对应 §1.4；105 对应 §1.5；106 对应 §1.6；107 对应 §1.7；108 对应 §1.8；109 对应 §1.9；110 对应 §1.10。000 是课程总览，000-ZSM 是补充实数基础。用户上传版本第一章印刷页 1–27 对应 PDF 第 13–39 页。

**教材只作参考，没有单独编写教材 notes，也没有将教材整本放入仓库。** 教材 §1.8 有其紧陪域、闭值等约定；不能将其结论移到一般空间后忽略相应条件。本讲义是辅助自学材料，不是教师官方讲义。原课件和教材著作权属于原作者；讲解不改变原材料权属。

## 从源码编译

在仓库根目录执行，不能在 `notes/` 子目录直接运行：

```bash
python3 scripts/build.py -j 3
# 单独编译
python3 scripts/build.py 108 -j 1
```

需要 Python 3、XeLaTeX（TeX Live，含基础及 recommended/extra 宏包）、Noto CJK 字体。Ubuntu/Debian 可安装：

```bash
sudo apt-get update
sudo apt-get install -y texlive-xetex texlive-latex-extra texlive-fonts-recommended fonts-noto-cjk
```

编译脚本执行两轮，生成可点击目录，保留失败命令的退出状态；中间文件在被忽略的 `build/` 中，成品在 `pdf/gpt-*.pdf`。正文在 `notes/*-body.tex`，统一排版与基础说明在 `tex/`。PDF 已提交，可直接阅读，无需自行安装 LaTeX。

覆盖检查另需 `PyMuPDF`（`python3 -m pip install PyMuPDF`），运行：

```bash
python3 scripts/validate.py
```

检查每本原页编号完整有序、编译 PDF 中包含原页表单、中文可提取且无字体缺字；`coverage.json` 保存原页数、成品页数及 SHA-256。该程序检验材料覆盖和构建完整性，不是数学正确性的自动证明器。公式排版另经人工抽样查看，证明中的条件与已发现的笔误在正文逐项说明。
