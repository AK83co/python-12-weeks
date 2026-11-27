"""
Week 10 · Exercise 1: Animal sounds

Animal is done. Make Dog and Cow subclasses whose speak() returns "Woof" and
"Moo".

Examples:
    Dog("Rex").speak()         →  "Woof"
    Cow("Daisy").describe()    →  "Daisy says Moo"

Check your answer:  python check.py 10 animal_sounds
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"

# write Dog and Cow here
