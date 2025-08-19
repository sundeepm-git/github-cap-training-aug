# Copilot Starter: Generate Code from Comments (Python)
# =====================================================
# Use this tiny file to see how GitHub Copilot turns comments/docstrings
# into working code. Open in VS Code with Copilot enabled.
#
# How to use:
# 1) Put your cursor where indicated below each task.
# 2) Press ENTER once and pause — Copilot should propose ghost text.
# 3) Press TAB to accept the suggestion (or use 'Show Next Suggestion' to cycle).
# 4) Run this file to test (Terminal > python copilot_from_comments_simple.py).
 
 
# -----------------------------
# Task 1: add(a, b) -> int
# Goal: Implement a simple adder using only the docstring below.
# -----------------------------
def add(a: int, b: int) -> int:
    """
    Return the sum of a and b as an integer.
    Example:
    >>> add(2, 3)
    5
    """
    return a + b
 
 
# -----------------------------
# Task 2: greet(name) -> str
# Goal: Generate a tiny function from two comment lines.
# -----------------------------
# Write a function greet(name: str) -> str
# It should return: "Hello, <name>!"
# Place the cursor on the next line, press ENTER, and pause.
def greet(name: str) -> str:
    return f"Hello, {name}!"
 
 
 
# -----------------------------
# Task 3 (optional): is_even(n) -> bool
# Goal: Show Copilot can do simple logic from natural language comments.
# -----------------------------
def is_even(n: int) -> bool:
    """
    Return True if n is an even integer, otherwise False.
    Rules:
    - Works for negative numbers.
    - 0 is even.
    Examples:
    >>> is_even(2)  # True
    >>> is_even(3)  # False
    """
    # Put the cursor here, press ENTER, and accept Copilot's multi-line suggestion.
    return n % 2 == 0
    pass
 
 
# -----------------------------
# Quick manual checks (after you accept Copilot's suggestions above)
# -----------------------------
if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))             # expect 5
    print("greet('Ada') =", greet("Ada"))      # expect Hello, Ada!
    print("is_even(10) =", is_even(10))         # expect True
    print("is_even(7) =", is_even(7))           # expect False
 