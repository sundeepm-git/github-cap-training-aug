import re
from collections import Counter
# Mini Demo: Using GitHub Copilot in VS Code (Python)
# --------------------------------------------------
# How to use this file:
# 1) Open this file in VS Code with the GitHub Copilot extension enabled.
# 2) For each TASK below:
#    - Place your cursor as indicated.
#    - Type the provided comment/docstring or starter signature.
#    - Pause briefly. Copilot will propose ghost text (multi-line suggestions).
#    - Press TAB to accept; ESC to dismiss; use 'Show Next/Previous Inline Suggestion' for alternatives.
# 3) If suggestions don't appear, open Command Palette → 'Copilot: Generate Inline Suggestion'.
#
# Pro tips:
# - Clear, specific comments = better code.
# - Include inputs/outputs, constraints, and examples in docstrings.
# - Build in small chunks: comment → accept → run → iterate.
 
 
# ==================================================
# TASK 1 — Generate code from a docstring
# Goal: Let Copilot implement a simple function by reading your docstring.
# ==================================================
 
def slugify(title: str) -> str:
    """
    Turn an arbitrary title into a URL-friendly slug.
    Rules:
    - Lowercase all characters.
    - Replace spaces and punctuation with a hyphen.
    - Collapse multiple consecutive hyphens into a single hyphen.
    - Trim leading and trailing hyphens.
    Examples:
    >>> slugify("Hello, World!")
    "hello-world"
    >>> slugify("  Python 3.12 — What's New? ")
    "python-3-12-what-s-new"
    """
        
    # Place your cursor on the next line, press ENTER once, and wait for Copilot.
    slug = title.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


# ==================================================
# TASK 2 — Generate code from a richer docstring (counts & sorting)
# Goal: Count words and return the top K most frequent words.
# ==================================================
 
def top_k_words(text: str, k: int) -> list[tuple[str, int]]:
    """
    Return the k most frequent words in the given text as (word, count) pairs.
    Requirements:
    - Case-insensitive (treat 'The' and 'the' the same).
    - Words are sequences of letters/numbers; ignore punctuation.
    - Break ties by alphabetical order of the word.
    - If k exceeds the number of unique words, return all words.
    Examples:
    >>> top_k_words("red red blue green RED", 2)
    [("red", 3), ("blue", 1)]
    >>> top_k_words("To be, or not to be: that is the question.", 3)
    [("be", 2), ("to", 2), ("or", 1)]
    """
    # Put the caret below and let Copilot suggest a full solution.
    text = text.lower()
    words = re.findall(r"\w+", text)
    counts = Counter(words)
    most_common = counts.most_common(k)
    return most_common

 
# ==================================================
# TASK 3 — Multi-line completion from a step list
# Goal: Give Copilot a sequence of steps; let it write the code.
# ==================================================
 
def load_numbers(path: str) -> list[float]:
    # Steps:
    # 1) Open the file at 'path' for reading (UTF-8).
    # 2) Read all lines; ignore empty lines and comments starting with '#'.
    # 3) Convert each remaining line to float; strip whitespace.
    # 4) Return a list of floats.
    # Place your cursor after the steps and wait for Copilot.
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    numbers = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            try:
                numbers.append(float(line))
            except ValueError:
                continue
    return numbers


def stats(numbers: list[float]) -> dict[str, float]:
    # Steps:
    # 1) If the list is empty, raise ValueError("no data").
    # 2) Compute count, mean, min, max.
    # 3) Compute population standard deviation.
    # 4) Return a dict: {"count": ..., "mean": ..., "min": ..., "max": ..., "stdev": ...}
    if not numbers:
        raise ValueError("no data")
    stats = {
        "count": len(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
    # Compute population standard deviation
    squared_diffs = [(x - stats["mean"]) ** 2 for x in numbers]
    stats["stdev"] = (sum(squared_diffs) / len(numbers)) ** 0.5
    return stats


# ==================================================
# TASK 4 — Inline suggestions while refactoring
# Goal: Start writing a loop; let Copilot finish idiomatic Python.
# ==================================================
 
def normalize_names(names: list[str]) -> list[str]:
    # intent: strip, lowercase, collapse multiple spaces to single, title-case each name
    # Try typing: result = []
    # Then start a for-loop: for n in names:
    # Keep typing hints like: cleaned = " ".join(n.strip().split()).lower()
    # and pause to see Copilot finish the rest.

    result = []
    for n in names:
        cleaned = " ".join(n.strip().split()).lower()
        result.append(cleaned.title())
    return result


# ==================================================
# TASK 5 — Small class from docstring
# Goal: Use a docstring to define a simple class with methods and validation.
# ==================================================
 
class Student:
    """
    Represent a student with a name and a list of numeric grades (0–100).
    - .add(grade): add a grade; invalid values raise ValueError.
    - .average(): return the average (0–100) or 0 for no grades.
    - .letter_grade(): return "A/B/C/D/F" based on average (>=90 A, >=80 B, ...).
    - __repr__ shows: Student(name='Alice', grades=[...])
    Examples:
    >>> s = Student("Alice"); s.add(95); s.add(82); s.letter_grade()
    "B"
    """
    # Place the caret and wait for Copilot to scaffold fields & methods.
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add(self, grade: float):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Invalid grade")

    def average(self) -> float:
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self) -> str:
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, grades={self.grades!r})"


# ==================================================
# TASK 6 — Quick tests (Copilot can draft them too)
# Goal: Let Copilot write simple unit tests from docstrings/comments.
# ==================================================
 
def _tests():
    """
    Quick non-pytest checks so you can run this file directly.
    - Verify slugify basic cases.
    - Verify top_k_words counts and ordering.
    - Verify load_numbers + stats with a small sample.
    - Verify Student behavior for letter grades.
    """
    s = Student("Alice")
    s.add(95)
    s.add(82)
    assert s.letter_grade() == "B"
    s.add(74)
    assert s.letter_grade() == "B"
    s.add(60)
    assert s.letter_grade() == "C"
    s.add(50)
    assert s.letter_grade() == "C"


if __name__ == "__main__":
    # You can run this file after accepting Copilot's suggestions.
    # python copilot_python_mini_demo.py
    print("Mini demo placeholder — run _tests() after you accept Copilot's code.")
    _tests()