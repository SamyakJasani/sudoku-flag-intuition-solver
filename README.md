# Flag-Based Sudoku Solver

This is a **console-based intuitive Sudoku solver** that mimics human-solving strategies using **logical flags**, before falling back to **brute-force backtracking**.  
It solves any 9x9 Sudoku puzzle step-by-step, printing the board after each logical pass.

---

## Features

- Detects all valid positions for each number using flagging logic  
- Uses hidden singles in rows, columns, and 3x3 boxes  
- Repeats logical inference until no progress is made  
- Switches to backtracking only when logic is exhausted  
- Fully in-Python with no external libraries  

---

## Why Flags Are Better Than Backtracking (Initially)

| Approach     | Characteristics |
|--------------|-----------------|
| **Flagging**     | Imitates human logic (hidden singles, pencil marks), faster for easier puzzles |
| **Backtracking** | Brute-force method: tries all valid numbers recursively |

Flagging first **reduces the search space**, and often solves:
- Easy & medium puzzles without recursion  
- Hard puzzles with fewer backtrack calls  
- Avoids stack overflows on larger boards  

---

## How to Run
python sudoku_bot.py
