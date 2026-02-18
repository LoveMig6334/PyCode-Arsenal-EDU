# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.12+, virtual environment at `.venv/`
- Activate: `.venv/Scripts/activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

## Running Code

```bash
# Run a standalone script
python playgrounds/BinarySearch.py
python "projects/3 Body Problem/main.py"
python "projects/MyPy Game/main.py"

# Open a notebook
jupyter notebook "classes/CAMP CD M3/basic PY AI/5. Scikit_learn.ipynb"
```

## Repository Structure

This is a personal educational Python repository with four main areas:

### `problem/` — Competitive Programming
Solutions for TOI Zero (2025 & 2026) and Pro-IN-TH. Each problem is a self-contained `.py` file. Problem statements are in the `(1) Website.md` files in each folder (external links to online judges).

### `projects/` — Standalone Projects
Each project lives in its own subdirectory with a `main.py` entry point.

- **`MyPy Game/`** — OOP terminal RPG. Architecture: `classpy/chr.py` defines the base `Character` class (attack, cast_spell, level_up); `classpy/mots.py` defines `Monster`; `main.py` defines `Mage` and `Warrior` subclasses and runs the game loop.
- **`3 Body Problem/`** — Gravitational n-body simulation using `scipy.integrate.solve_ivp` + `matplotlib` animation.
- **`Prime Timer/`** — Benchmark comparing single-process (`main.py`) vs multiprocessing (`multi_main.py`) prime generation.
- **`Pass Genarator/`**, **`RSSI Plot/`**, **`irem888/`**, **`kumu chikenanrice/`** — Single-file or simple projects.

### `playgrounds/` — Concept Drills
Isolated scripts for algorithms and Python language features. No shared dependencies between files.

### `classes/` — Coursework & Camps

- **`COM M3/`** — M3 class exercises (basic Python scripts)
- **`COM M4/`** — M4 class work:
  - `Python Data/` — Jupyter notebooks on list, set, dict, tuple, types
  - `Game/Panpaa/` — Coin-flip game assignment (notebook)
  - `Python OOP/` — Chicken-rice shop OOP assignments (Work 21–23, multi-part series)
  - `Final/` — Final project: "The Dragon's Cave" text RPG
- **`CAMP CD M3/`** — Data Science & AI camp:
  - `basic PY AI/` — Sequential Jupyter notebooks (1–5): Python → Pandas → Scikit-learn
  - `project/` — Three ML projects: text classification, text regression, information retrieval
- **`CAMP NSC 2025/`** — National Software Contest camp:
  - `ipynb/` — NSC-Tutorial.ipynb (Python fundamentals) and NSC-PyTorch.ipynb (deep learning)
  - `test/` — Numbered exercise scripts (3–9): Lists, Dicts, Conditionals, Loops, Functions, OOP, File Handling

## Key Libraries

| Library | Use |
|---|---|
| `numpy` | Numerical arrays, simulations |
| `matplotlib` | Plotting, animations |
| `scipy` | ODE solving (3-body problem) |
| `pandas` | Data wrangling (camp notebooks) |
| `scikit-learn` | ML (camp projects) |
| `opencv-python` | Image processing (where used) |
| `pyperclip` | Clipboard (Pass Generator) |
