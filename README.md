# 个人简历项目 - 马驰原

LaTeX 简历的模板与构建工具链。

**本仓库只包含去除了个人信息的模板**（位于 `example/`）。真实简历含手机号、住址等个人信息，
不纳入版本库——这样仓库可以公开，而真实内容只留在本地。

## 项目结构

仓库内实际包含：

- `example/resume_cn.tex`: 中文简历模板（占位内容，3410 字节）。
- `example/resume_en.tex`: 英文简历模板（占位内容，3009 字节）。
- `watch.py`: 自动编译脚本，监控 `.tex` 文件更改并实时重新生成 PDF。
- `sync.sh`: GitHub 同步脚本，方便一键提交。
- `LICENSE`: MIT。

本地工作副本中还会存在以下文件，均已被 `.gitignore` 排除：

- `resume_cn.tex` / `resume_en.tex`: 填入真实信息后的简历源码。
- `resume_cn.pdf` / `resume_en.pdf` / `resume_combined.pdf`: 编译产物。
- 简历用个人照片。

## 环境要求

- **Tectonic**: 一个现代、自包含的 TeX/LaTeX 引擎。
- **pdfunite** (来自 `poppler-utils`): 用于合并 PDF 文件。
- **Python 3**: 运行自动编译脚本所需。

## 使用方法

### 初始化

把模板复制到仓库根目录，再填入自己的信息：

```bash
cp example/resume_en.tex resume_en.tex
cp example/resume_cn.tex resume_cn.tex
```

### 手动编译

```bash
# 编译英文版
tectonic resume_en.tex

# 编译中文版
tectonic resume_cn.tex
```

如果使用独立的 LaTeX 环境，把 `tectonic` 换成对应路径，例如
`~/miniconda3/envs/latex_env/bin/tectonic`。

### 自动监视编译

运行监视脚本，保存 `.tex` 文件时将自动重新编译：

```bash
python3 watch.py
```

该脚本会：

1. 检测 `resume_en.tex` 或 `resume_cn.tex` 的更改。
2. 使用 `tectonic` 重新编译更新的文件。
3. 将两个版本合并为 `resume_combined.pdf`。

### 同步到 GitHub

```bash
./sync.sh "更新了实习经历细节"
```

## 自定义配置

- **字体大小**: 主标题、公司名、项目名设置为 **12pt**；教育背景标签设置为 **11pt**。
- **个人信息**: 保持两版信息一致且简洁。
- **布局**: 两版均经过精细调整，确保信息密度高且视觉美观，各占一页。

---

# CV Project - MA CHIYUAN (English Summary)

A LaTeX-based CV toolchain. This repository ships **templates only** (`example/`);
the real resumes contain personal contact details and are intentionally excluded from
version control.

## Quick Start

1.  **Init**: `cp example/resume_en.tex resume_en.tex` (and the Chinese counterpart).
2.  **Compile**: `tectonic resume_en.tex` / `tectonic resume_cn.tex`.
3.  **Auto-build**: `python3 watch.py` monitors changes and rebuilds.
4.  **Sync**: `./sync.sh` pushes updates.

Refer to the Chinese section above for full details.

## License

MIT — see [LICENSE](LICENSE).
