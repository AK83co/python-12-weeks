"""
Week 10 · Exercise 2: 2D vectors

Make a Vector class with x and y. Support + (add matching parts), ==, and a
__repr__ that shows Vector(x, y).

Examples:
    Vector(1, 2) + Vector(3, 4)   →  Vector(4, 6)
    Vector(1, 1) == Vector(1, 1)  →  True

Check your answer:  python check.py 10 2d_vectors
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
