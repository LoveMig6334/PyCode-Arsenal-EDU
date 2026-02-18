# PyCode-Arsenal-EDU

A comprehensive Python learning repository covering competitive programming, data science, machine learning, and project-based development — built through hands-on classwork, camps, and self-study.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Contents](#contents)
  - [Problem Solving](#-problem-solving)
  - [Projects](#-projects)
  - [Playgrounds](#-playgrounds)
  - [Classes & Camps](#-classes--camps)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)

---

## Overview

This repository is a personal educational arsenal covering multiple layers of Python development:

- **Competitive Programming** — TOI Zero (2025 & 2026) and Pro-IN-TH solutions
- **Applied Projects** — Physics simulations, games, data tools, and more
- **Data Science & ML** — Pandas, Scikit-learn, PyTorch notebooks from camps
- **Playgrounds** — Focused experiments on Python concepts and algorithms

---

## Repository Structure

```
PyCode-Arsenal-EDU/
├── problem/                    # Competitive programming solutions
│   ├── TOI Z 2025/             # TOI Zero 2025  (A1: 40, A2: 18, A3: 2)
│   ├── TOI Z 2026/             # TOI Zero 2026  (A1, A2)
│   └── Pro-IN-TH/              # Pro In Thailand problems
│
├── projects/                   # Standalone Python projects
│   ├── 3 Body Problem/         # Gravitational 3-body simulation (SciPy + Matplotlib)
│   ├── gravity-plot/           # Orbital mechanics visualizer
│   ├── MyPy Game/              # OOP-based terminal RPG
│   ├── Prime Timer/            # Multiprocessing prime benchmark
│   ├── Pass Generator/         # Password generator
│   ├── RSSI Plot/              # Signal-strength plotter
│   ├── irem888/                # Coin-toss probability simulator
│   └── kumu chikenanrice/      # Chicken-rice shop ordering system
│
├── playgrounds/                # Quick experiments and concept drills
│
├── classes/                    # Coursework and camp materials
│   ├── COM M3/                 # M3 computer science class exercises
│   ├── CAMP CD M3/             # Camp CD M3 — Data Science & AI
│   │   ├── basic PY AI/        # Jupyter notebooks (Pandas, Scikit-learn)
│   │   ├── test/               # Practice scripts (basic + data-sci)
│   │   └── project/            # ML projects (text classification, regression, IR)
│   └── CAMP NSC 2025/          # NSC Camp 2025 — ML & PyTorch
│       ├── ipynb/              # NSC-Tutorial & NSC-PyTorch notebooks
│       └── test/               # Python fundamentals exercises
│
├── requirements.txt
└── README.md
```

---

## Contents

### Problem Solving

| Folder | Competition | Problems Solved |
|---|---|---|
| `TOI Z 2025/A1 (40)` | TOI Zero 2025 — Level A1 | 40 |
| `TOI Z 2025/A2 (18)` | TOI Zero 2025 — Level A2 | 18 |
| `TOI Z 2025/A3 (2)` | TOI Zero 2025 — Level A3 | 2 |
| `TOI Z 2026/A1 (40)` | TOI Zero 2026 — Level A1 | 9+ |
| `TOI Z 2026/A2 (20)` | TOI Zero 2026 — Level A2 | 1+ |
| `Pro-IN-TH/` | Pro In Thailand | 9+ |

### Projects

| Project | Description | Key Libraries |
|---|---|---|
| **3 Body Problem** | Gravitational n-body simulation with animation | `scipy`, `matplotlib`, `numpy` |
| **gravity-plot** | Orbital mechanics visualizer | `matplotlib` |
| **MyPy Game** | OOP terminal RPG with character and monster classes | — |
| **Prime Timer** | Multi-process prime-number benchmark | `multiprocessing` |
| **Pass Generator** | Configurable password generator | — |
| **RSSI Plot** | Real-time signal strength plotter | `matplotlib` |
| **irem888** | Coin-toss probability simulator with Jupyter analysis | `numpy` |
| **kumu chikenanrice** | Chicken-rice shop system with ordering & daily summary | — |

### Playgrounds

Isolated scripts for drilling Python fundamentals and algorithms:

| Topic | Files |
|---|---|
| Algorithms | `BinarySearch.py`, `Prime Number.py`, `Factorial.py` |
| Data Structures | `ListLearn.py`, `LoopList.py`, `sum-matrix.py` |
| Python Concepts | `decorator_ex.py`, `scope.py`, `zip_func.py`, `unppack.py`, `memory-id_ex.py` |
| Pattern Problems | `Diamond.py`, `Ladder.py`, `StairFnc.py` |
| Concurrency | `multi-cpu.py` |

### Classes & Camps

**CAMP CD M3** — Data Science & AI Camp

| Notebook | Topic |
|---|---|
| `1. Hello_python.ipynb` | Python basics |
| `2. Data_structure.ipynb` | Lists, dicts, arrays |
| `3. KungFu_Pandas.ipynb` | Pandas data wrangling |
| `4. Pandas_basic_stat.ipynb` | Descriptive statistics |
| `5. Scikit_learn.ipynb` | ML fundamentals |
| `project/text_classification` | Sentiment & spam classification |
| `project/text_regression` | Hotel review score prediction |
| `project/information_retrieval` | Article search / IR pipeline |

**CAMP NSC 2025** — National Software Contest Camp

| Resource | Description |
|---|---|
| `NSC-Tutorial.ipynb` | Python fundamentals notebook |
| `NSC-PyTorch.ipynb` | Intro to PyTorch & deep learning |
| `test/` | Exercises: Lists, Dicts, Loops, Functions, OOP, File Handling |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-2.4-013243?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-11557c)
![SciPy](https://img.shields.io/badge/SciPy-1.17-8CAAE6?logo=scipy)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn)
![PyTorch](https://img.shields.io/badge/PyTorch-DL-EE4C2C?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13-5C3EE8?logo=opencv)

---

## Getting Started

### Prerequisites

- Python 3.12 or higher
- `pip` package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/PyCode-Arsenal-EDU.git
cd PyCode-Arsenal-EDU

# 2. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Running Examples

```bash
# Run a playground script
python playgrounds/BinarySearch.py

# Run a project
python "projects/3 Body Problem/main.py"

# Open a Jupyter notebook
jupyter notebook "classes/CAMP CD M3/basic PY AI/5. Scikit_learn.ipynb"
```

---

## Dependencies

```
matplotlib==3.10.8
numpy==2.4.2
pandas==3.0.1
scipy==1.17.0
opencv-python==4.13.0.92
pillow==12.1.1
pyperclip==1.11.0
```

> For the full pinned list see [`requirements.txt`](requirements.txt).
