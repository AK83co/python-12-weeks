# Week 9 project: Virtual pet
#
# Create a pet that gets hungry and bored over time. Feed it and play with it
# to keep it happy.
#
# Milestones:
#   1. Write a Pet class with name, hunger and happiness attributes
#   2. Add feed(), play() and status() methods
#   3. Add a tick() method that makes the pet hungrier and less happy each turn
#   4. Build a game loop: each turn, show status and ask what to do
#   5. End the game if hunger or happiness reaches a limit
#   6. Add __str__ so print(pet) shows a little face like (^_^) or (T_T)
#
# Run it:  python weeks/week09_classes_and_objects/project.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 3
        self.happiness = 5

    def feed(self):
        self.hunger = max(0, self.hunger - 3)

    def status(self):
        return f"{self.name}: hunger {self.hunger}/10, happiness {self.happiness}/10"

pet = Pet(input("Name your pet: "))
print(pet.status())
