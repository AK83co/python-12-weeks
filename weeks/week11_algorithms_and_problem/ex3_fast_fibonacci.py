"""
Week 11 · Exercise 3: Fast Fibonacci

Write fib(n): fib(0) = 0, fib(1) = 1, and each next one is the sum of the
two before. It must handle fib(80) quickly; the obvious recursive version
will run out of time!

Examples:
    fib(10)  →  55
    fib(80)  →  23416728348467685

Check your answer:  python check.py 11 fast_fibonacci
"""

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)   # too slow for big n!
