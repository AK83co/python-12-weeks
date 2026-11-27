# Week 2 project: Choose-your-own-adventure
#
# A short text adventure where the player's choices lead to different endings.
#
# Milestones:
#   1. Write an opening scene and ask the player to choose (A or B)
#   2. Use if / elif / else to send them down different paths
#   3. Add a second choice inside at least one path (an if inside an if)
#   4. Write at least 3 different endings
#   5. Handle typos: tell the player when they type something unexpected
#   6. Use .lower() so “A” and “a” both work
#
# Run it:  python weeks/week02_making_decisions/project.py

print("You wake up in a dark forest. Paths lead LEFT and RIGHT.")
choice = input("Which way? (left/right) ").lower()

if choice == "left":
    print("You find a sleeping dragon...")
    # ask another question here!
elif choice == "right":
    print("You reach a river with a small boat.")
else:
    print("You stand still until night falls. The end.")
