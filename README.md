# 个人简历项目 - 马驰原

本项目包含了使用 LaTeX 编写的马驰原的中英文个人简历。项目旨在通过自动化工具维护简历的高效更新与多版本整理。

## 项目结构

- `resume_cn.tex`: 中文简历源码文件。
- `resume_en.tex`: 英文简历源码文件。
- `resume_cn.pdf`: 生成的中文简历（已加入 `.gitignore`，需本地编译）。
- `resume_en.pdf`: 生成的英文简历（已加入 `.gitignore`，需本地编译）。
- `resume_combined.pdf`: 合并后的 PDF（英文在前，中文在后）。
- `watch.py`: 自动编译脚本，监控 `.tex` 文件更改并实时重新生成 PDF。
- `sync.sh`: GitHub 同步脚本，方便一键提交代码。
- `example/`: 简历模板目录，去除了个人信息，供参考使用。
- `本科毕业证件照.jpg`: 简历中使用的个人照片预览。

## 环境要求

- **Tectonic**: 一个现代、自包含的 TeX/LaTeX 引擎。
- **pdfunite** (来自 `poppler-utils`): 用于合并 PDF 文件。
- **Python 3**: 运行自动编译脚本所需。

## 使用方法

### 手动编译

手动编译特定版本：

```bash
# 编译英文版
~/miniconda3/envs/latex_env/bin/tectonic resume_en.tex

# 编译中文版
~/miniconda3/envs/latex_env/bin/tectonic resume_cn.tex
```

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

使用提供的脚本快速提交更改：

```bash
./sync.sh "更新了实习经历细节"
```

## 自定义配置

- **字体大小**: 主标题、公司名、项目名设置为 **12pt**；教育背景标签设置为 **11pt**。
- **个人信息**: 保持两版信息一致且简洁。
- **布局**: 两版均经过精细调整，确保信息密度高且视觉美观，各占一页。

---

# CV Project - MA CHIYUAN (English Summary)

This project maintains LaTeX source files for professional CVs in both English and Chinese.

## Quick Start

1.  **Compile**: Use `tectonic resume_en.tex` or `tectonic resume_cn.tex`.
2.  **Auto-build**: Run `python3 watch.py` to monitor changes.
3.  **Sync**: Run `./sync.sh` to push updates to your repository.

Refer to the Chinese section above for full details.
