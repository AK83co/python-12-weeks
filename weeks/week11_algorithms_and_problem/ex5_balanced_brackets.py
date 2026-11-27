"""
Week 11 · Exercise 5: Balanced brackets

Write is_balanced(text) that returns True if every ( [ { is closed by its
matching ) ] } in the right order. Ignore other characters. (Hint: a list
can work as a stack.)

Examples:
    is_balanced("([]{})")      →  True
    is_balanced("([)]")        →  False
    is_balanced("print(x[0])")  →  True

Check your answer:  python check.py 11 balanced_brackets
"""

def is_balanced(text):
    stack = []
    return True
