# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a student workspace containing two Git-tracked projects and a LaTeX document project, all located under `OneDrive/Desktop/`.

## Projects

### COMP_EXTRA — Competitive Programming (CSES Problem Set)
- **Path:** `OneDrive/Desktop/COMP_EXTRA/`
- **Repo:** https://github.com/Tchniber1/COMP_EXTRA.git
- Solutions to CSES competitive programming problems in Python
- All solutions live in `CSES/` subdirectory
- Solutions read from stdin and print to stdout (standard competitive programming I/O)
- Modular arithmetic uses `MOD = 10**9 + 7` where needed

### SASE_COMP101 — CS Course
- **Path:** `OneDrive/Desktop/SASE_COMP101/`
- **Repo:** https://github.com/Tchniber1/SASE_COMP101.git
- Weekly coursework organized by `WEEK N/` directories
- Mix of Jupyter Notebooks (`.ipynb`) for assignments and standalone Python scripts

### LaTeX Math Summary
- **Path:** `OneDrive/Desktop/Latex/math_summary/`
- Compiled with MiKTeX (`math(3).tex` is the latest source)

## Running Code

```bash
# Run a Python script
python "OneDrive/Desktop/COMP_EXTRA/CSES/exex.py"

# Jupyter notebooks — open in Jupyter or VS Code
jupyter notebook "OneDrive/Desktop/SASE_COMP101/WEEK 3/exercises.ipynb"

# Compile LaTeX
cd "OneDrive/Desktop/Latex/math_summary" && pdflatex "math(3).tex"
```

## Environment

- **Python** installed system-wide (no virtualenv or requirements.txt)
- **MiKTeX** for LaTeX compilation
- **Git** configured for user Tchniber1
- Paths contain spaces (e.g., `WEEK 2/`) — always quote paths in shell commands
