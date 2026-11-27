"""
Week 5 · Exercise 1: Power with a default

Write power(base, exp=2) that returns base to the power exp. If exp isn't
given, square the number.

Examples:
    power(5)      →  25
    power(2, 10)  →  1024

Check your answer:  python check.py 5 power_with_a_default
"""

def power(base, exp):
    return base ** exp
