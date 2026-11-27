# Week 8: Errors, modules and debugging

Stop crashes, find bugs, and use code other people wrote.

**Goals:** Read a traceback · try / except · raise your own errors · import modules

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_safe_division.py` | `python check.py 8 safe_division` |
| `ex2_forgiving_number_reader.py` | `python check.py 8 forgiving_number_reader` |
| `ex3_validate_an_age.py` | `python check.py 8 validate_an_age` |
| `ex4_hypotenuse.py` | `python check.py 8 hypotenuse` |

Check the whole week at once: `python check.py 8`

## Project: Rock, paper, scissors

Play best-of-five against the computer, with a scoreboard and input that can't crash the game. Month 2 capstone!

Run it with `python weeks/week08_errors_modules_and/project.py`

- [ ] Let the computer choose with random.choice
- [ ] Write a winner(player, computer) function that returns 'player', 'computer' or 'draw'
- [ ] Keep score and play until someone has 3 wins
- [ ] Reject invalid choices without crashing
- [ ] Show the final result and offer a rematch

**Stretch goal:** Add lizard and Spock, or make the computer learn which move you pick most.
