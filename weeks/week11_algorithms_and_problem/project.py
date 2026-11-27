# Week 11 project: Hangman
#
# The classic word-guessing game, built carefully with functions and good
# structure.
#
# Milestones:
#   1. Pick a random word from a list
#   2. Show the word as underscores, revealing guessed letters
#   3. Track guessed letters in a set and reject repeats
#   4. Count wrong guesses and draw the hangman with text art
#   5. Detect win and loss
#   6. Split your code into small functions (display, check_guess, is_won)
#
# Run it:  python weeks/week11_algorithms_and_problem/project.py

import random

words = ["python", "variable", "function", "loop", "dictionary"]
word = random.choice(words)
guessed = set()
lives = 6

def display(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

while lives > 0:
    print(display(word, guessed), f"  lives: {lives}")
    letter = input("Guess a letter: ").lower()
    guessed.add(letter)
    if letter not in word:
        lives -= 1
    # check for a win here
