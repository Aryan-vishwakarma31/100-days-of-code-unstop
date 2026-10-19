# 🐍 Unstop 100-Day Coding Sprint

[![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Progress](https://img.shields.io/badge/Progress-Day_1_%2F_100-brightgreen?style=for-the-badge)](#-daily-progress-log)
[![Platform](https://img.shields.io/badge/Platform-Unstop-blue?style=for-the-badge)](https://unstop.com/)

> Documenting my daily progress and Python solutions for the **100-Day Coding Sprint** on Unstop.  
> The goal is to master Data Structures, Algorithms, and problem-solving to prepare for technical interviews! 🚀

---

## 📊 Challenge Summary

* **Start Date:** October 19, 2026
* **Language:** Python 3
* **Target:** 100 Days / 300+ Problems

---

## 📅 Daily Progress Log

### 🔹 Day 1: Array, Strings

| Problem Title | Difficulty | Points | Solution Code |
| :--- | :---: | :---: | :---: |
| **CHESSBOARD** | Easy | 100 | [chessboard.py](./Day-01-Array-Strings/chessboard.py) |
| **Exchanging Gifts** | Easy | 100 | [exchanging_gifts.py](./Day-01-Array-Strings/exchanging_gifts.py) |
| **Distinct K** | Easy | 100 | [distinct_k.py](./Day-01-Array-Strings/distinct_k.py) |

---

## 🛠️ How to Run Locally

Clone the repository and run any script using Python. Example commands:

```bash
# Clone repository
git clone https://github.com/Aryan-vishwakarma31/100-days-of-code-unstop.git

# Navigate into folder
cd 100-days-of-code-unstop/Day-01-Array-Strings

# Run solution (either pass the input as an argument or via stdin)
python chessboard.py a1
# or
echo "a1" | python chessboard.py
```

### Input formats (supported)
- chessboard.py: accepts a single coordinate token like `a1` (case-insensitive). Returns `Black` or `White`.
- distinct_k.py: supports either:
  - first line: `n k` then second line: `s1 s2 ... sn`
  - or token stream: `n s1 s2 ... sn k`
  Prints the k-th distinct string (order-preserving) or `-1` if not found.
- exchanging_gifts.py: supports either:
  - first line: `n m` followed by `m` pairs `a b` (on following lines or same line)
  - or token stream: `n m a1 b1 a2 b2 ...`
  Prints the index of the "judge" (person with in_degree == n-1 and out_degree == 0) or `-1`.

---

## Tests

I added a small pytest-compatible test suite under `tests/` (run `pytest` from the repo root to run them).

---

If you'd like, I can open a PR to add CI (GitHub Actions) to run tests automatically on push.
