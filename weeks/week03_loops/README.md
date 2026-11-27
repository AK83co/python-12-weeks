# Week 3: Loops

Repeat things without copying and pasting.

**Goals:** for loops with range() · Loop over text · while loops · The accumulator pattern

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_add_them_up.py` | `python check.py 3 add_them_up` |
| `ex2_count_the_vowels.py` | `python check.py 3 count_the_vowels` |
| `ex3_fizzbuzz.py` | `python check.py 3 fizzbuzz` |
| `ex4_reverse_it.py` | `python check.py 3 reverse_it` |
| `ex5_power_of_two.py` | `python check.py 3 power_of_two` |

Check the whole week at once: `python check.py 3`

## Project: Number guessing game

The computer picks a secret number from 1 to 100. The player guesses and gets “higher” or “lower” hints until they find it.

Run it with `python weeks/week03_loops/project.py`

- [ ] Pick a secret number with random.randint(1, 100)
- [ ] Use a while loop to keep asking for guesses
- [ ] Say “Too high” or “Too low” after each guess
- [ ] Count the guesses and show the total when they win
- [ ] Add a Play again? option
- [ ] Limit the player to 7 guesses

**Stretch goal:** Add difficulty levels (1–10, 1–100, 1–1000) and keep track of the best score across rounds.
