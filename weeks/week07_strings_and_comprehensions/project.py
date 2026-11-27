# Week 7 project: Password toolkit
#
# A program that checks how strong a password is and can generate strong new
# ones.
#
# Milestones:
#   1. Write check_strength(pw) that scores length, digits, upper case, lower case and symbols
#   2. Print a rating (weak / okay / strong) with tips on what's missing
#   3. Write generate(length) using random.choice on a string of allowed characters
#   4. Make sure generated passwords always include at least one of each type
#   5. Add a menu: check / generate / quit
#
# Run it:  python weeks/week07_strings_and_comprehensions/project.py

import random

def check_strength(pw):
    score = 0
    if len(pw) >= 12: score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    # add lower case and symbol checks
    return score

def generate(length=14):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    return "".join([random.choice(chars) for _ in range(length)])

print(generate())
print(check_strength("hunter2"))
