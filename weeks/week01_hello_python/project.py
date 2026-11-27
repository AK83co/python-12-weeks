# Week 1 project: Mad Libs story generator
#
# Ask the player for some words, then print a silly story using them. Your
# first interactive program!
#
# Milestones:
#   1. Ask for at least 4 words with input() (an adjective, an animal, a place, a food…)
#   2. Store each answer in a well-named variable
#   3. Print a 3–4 sentence story using f-strings
#   4. Add a title line and make the output look tidy
#   5. Show it to someone and let them play
#
# Run it:  python weeks/week01_hello_python/project.py

print("=== MAD LIBS ===")
adjective = input("Give me an adjective: ")
animal = input("Name an animal: ")
place = input("Name a place: ")

print()
print(f"Once upon a time, a {adjective} {animal} lived in {place}.")
# Keep the story going...
