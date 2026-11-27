"""
Week 2 · Exercise 2: Letter grade

Write grade(score) that returns a letter: 90 or more → "A", 80+ → "B", 70+ →
"C", 60+ → "D", anything lower → "F".

Examples:
    grade(95)  →  "A"
    grade(72)  →  "C"
    grade(40)  →  "F"

Check your answer:  python check.py 2 letter_grade
"""

def grade(score):
    if score >= 90:
        return "A"
    # keep going...
