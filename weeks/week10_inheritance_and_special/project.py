# Week 10 project: Text adventure engine
#
# Build a small world of connected rooms using classes, with items to pick up
# and a goal to reach.
#
# Milestones:
#   1. Write a Room class with a name, description and exits (a dict like {'north': other_room})
#   2. Create at least 4 rooms and connect them
#   3. Write a Player class that tracks the current room and an inventory list
#   4. Read commands like 'go north', 'take key' and 'look'
#   5. Add a locked room that needs an item to enter
#   6. Add a way to win
#
# Run it:  python weeks/week10_inheritance_and_special/project.py

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

hall = Room("Hall", "A dusty hallway.")
kitchen = Room("Kitchen", "Smells like old soup.")
hall.exits["north"] = kitchen
kitchen.exits["south"] = hall
kitchen.items.append("key")

current = hall
while True:
    print(f"\n{current.name}: {current.description}")
    cmd = input("> ").lower().split()
    if not cmd: continue
    if cmd[0] == "quit": break
    if cmd[0] == "go" and len(cmd) > 1 and cmd[1] in current.exits:
        current = current.exits[cmd[1]]
