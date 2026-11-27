# Week 6 project: Gradebook
#
# Keep track of students and their marks: add grades, see averages, and find
# the top student.
#
# Milestones:
#   1. Store students in a dict: name → list of grades
#   2. Add a command to add a student
#   3. Add a command to add a grade for a student
#   4. Show each student's average
#   5. Find and print the top student
#   6. Show a letter grade next to each average (reuse your week 2 grade function!)
#
# Run it:  python weeks/week06_dictionaries_and_sets/project.py

grades = {"Ada": [90, 85], "Alan": [72, 88]}

def average(nums):
    return sum(nums) / len(nums) if nums else 0

while True:
    cmd = input("add / grade / report / quit: ")
    if cmd == "report":
        for name, marks in grades.items():
            print(f"{name}: {average(marks):.1f}")
    elif cmd == "quit":
        break
    # add the other commands
