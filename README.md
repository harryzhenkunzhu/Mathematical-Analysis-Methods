# Mathematical Analysis Methods｜数理分析方法

这是张顺明教授《数理分析方法》12 份课件的自学笔记项目索引。

目前 ChatGPT 会话中已生成 **12 个可编译的 LaTeX 讲义、12 个 PDF、原始 12 份 PPT 和构建脚本**，共对应 **657 页课件**。完整初稿可在对应 ChatGPT 会话下载 ZIP 文件。本仓库暂时仅含项目说明；**完整文件尚未直接上传到 GitHub**，不能把这个仓库当作已完整发布的版本。

## 目录

| PPT | 页数 | 主要主题 |
|---|---:|---|
| 000-PPT | 19 | 课程与一般均衡导论 |
| 000-ZSM-PPT | 62 | 实数理论基本定理 |
| 101-ZSM-PPT | 10 | 数学基础导论 |
| 102-ZSM-PPT | 53 | 集合 |
| 103-ZSM-PPT | 35 | 函数与对应 |
| 104-ZSM-PPT | 29 | 预序与偏好 |
| 105-ZSM-PPT | 67 | 实数 |
| 106-ZSM-PPT | 100 | 欧氏空间与极限 |
| 107-ZSM-PPT | 43 | 连续函数 |
| 108-ZSM-PPT | 113 | 连续对应 |
| 109-ZSM-PPT | 118 | 向量与凸分析 |
| 110-ZSM-PPT | 8 | 不动点定理 |

## 初稿完成程度

每份 PDF 都完整嵌入了对应课件的每一页，并提供中文阅读提示与相关的证明专题。**这仍是初稿**：并非每页都有独立、充分深入的讲解，部分阅读提示基于主题分类自动生成；也没有核查完 PPT 中全部证明，高维 Brouwer 与 Kakutani 的完整证明尚未编写。使用时仍须对照原 PPT。

*Theory of Value* (Gérard Debreu, 1959) 是参考教材，不另写笔记，也不重新发布扫描版。

## 下载、编译

完整初稿的 ZIP 文件来自本次 ChatGPT 会话，而非本仓库当前文件。解压后在项目根目录运行：

```bash
python3 -m pip install pymupdf
python3 build_notes.py
cd tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=../_build 110-ZSM-PPT.tex
```

须安装 XeLaTeX/ctex 和常用字体。