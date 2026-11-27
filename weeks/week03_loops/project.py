# Week 3 project: Number guessing game
#
# The computer picks a secret number from 1 to 100. The player guesses and
# gets “higher” or “lower” hints until they find it.
#
# Milestones:
#   1. Pick a secret number with random.randint(1, 100)
#   2. Use a while loop to keep asking for guesses
#   3. Say “Too high” or “Too low” after each guess
#   4. Count the guesses and show the total when they win
#   5. Add a Play again? option
#   6. Limit the player to 7 guesses
#
# Run it:  python weeks/week03_loops/project.py

import random

secret = random.randint(1, 100)
guesses = 0
print("I'm thinking of a number from 1 to 100.")

while True:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess == secret:
        print(f"Correct! You got it in {guesses} guesses.")
        break
    # add the too high / too low hints here
