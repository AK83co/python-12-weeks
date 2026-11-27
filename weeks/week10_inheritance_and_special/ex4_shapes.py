"""
Week 10 · Exercise 4: Shapes

Make Square(side) and Circle(radius) subclasses of Shape, each with an
area() rounded to 2 decimals. Use math.pi for circles.

Examples:
    Square(3).area()  →  9
    Circle(1).area()  →  3.14

Check your answer:  python check.py 10 shapes
"""

import math

class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"{type(self).__name__} with area {self.area()}"
