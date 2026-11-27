# Week 4 project: Terminal to-do list
#
# A menu-driven to-do app: add tasks, show them, tick them off, and quit.
# Month 1 capstone!
#
# Milestones:
#   1. Show a menu in a loop: add / show / done / quit
#   2. Add tasks to a list
#   3. Show tasks numbered from 1 (use enumerate)
#   4. Mark a task done by its number (remove it, or move it to a done list)
#   5. Handle bad input, like a number that isn't in the list
#   6. Show how many tasks are left
#
# Run it:  python weeks/week04_lists_and_tuples/project.py

tasks = []

while True:
    action = input("add / show / done / quit: ").lower()
    if action == "add":
        task = input("Task: ")
        tasks.append(task)
    elif action == "show":
        for i, t in enumerate(tasks):
            print(f"{i + 1}. {t}")
    elif action == "quit":
        print("Bye!")
        break
    # add "done" here
