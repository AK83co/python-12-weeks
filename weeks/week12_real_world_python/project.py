# Week 12 project: Capstone: your own app
#
# Build one bigger project on your own computer, using everything from the
# course. Pick an idea below or invent one: an expense tracker that saves to
# CSV, a quiz app that loads questions from JSON, a weather checker using
# requests, a Flask website, or a pygame game.
#
# Milestones:
#   1. Install Python and VS Code on your computer and run a hello-world file
#   2. Choose your project and write a one-paragraph plan of what it does
#   3. List the features: must-have first, nice-to-have later
#   4. Build the smallest working version
#   5. Save data to a file so it remembers between runs
#   6. Use at least one class and handle errors with try / except
#   7. Put it on GitHub with a README describing it
#   8. Show it to someone and ask for feedback
#
# Run it:  python weeks/week12_real_world_python/project.py

# expense_tracker.py: a starting point to run on your own computer
import csv
from datetime import date

FILE = "expenses.csv"

def add_expense(item, cost):
    with open(FILE, "a", newline="") as f:
        csv.writer(f).writerow([date.today(), item, cost])

def total():
    try:
        with open(FILE) as f:
            return sum(float(row[2]) for row in csv.reader(f))
    except FileNotFoundError:
        return 0

add_expense("coffee", 3.50)
print("Total spent:", total())
