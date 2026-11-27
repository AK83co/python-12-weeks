# Week 8 project: Rock, paper, scissors
#
# Play best-of-five against the computer, with a scoreboard and input that
# can't crash the game. Month 2 capstone!
#
# Milestones:
#   1. Let the computer choose with random.choice
#   2. Write a winner(player, computer) function that returns 'player', 'computer' or 'draw'
#   3. Keep score and play until someone has 3 wins
#   4. Reject invalid choices without crashing
#   5. Show the final result and offer a rematch
#
# Run it:  python weeks/week08_errors_modules_and/project.py

import random

options = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def winner(player, computer):
    if player == computer:
        return "draw"
    if beats[player] == computer:
        return "player"
    return "computer"

player = input("rock, paper or scissors? ").lower()
computer = random.choice(options)
print("Computer chose", computer)
print("Winner:", winner(player, computer))
