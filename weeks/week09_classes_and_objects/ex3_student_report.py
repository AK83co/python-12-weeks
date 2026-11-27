"""
Week 9 · Exercise 3: Student report

Make a Student class with a name, an empty list of grades, an add_grade(g)
method, and an average() method that returns the average rounded to 1
decimal (0 if there are no grades).

Examples:
    s = Student("Ada")
    s.add_grade(90); s.add_grade(85)
    s.average()  →  87.5

Check your answer:  python check.py 9 student_report
"""

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
