# Week 2: Making decisions

Let your programs react to input with if, elif and else.

**Goals:** Read user input · Convert between types · Compare values · Use if / elif / else

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_even_or_odd.py` | `python check.py 2 even_or_odd` |
| `ex2_letter_grade.py` | `python check.py 2 letter_grade` |
| `ex3_biggest_of_three.py` | `python check.py 2 biggest_of_three` |
| `ex4_leap_year.py` | `python check.py 2 leap_year` |
| `ex5_cinema_ticket.py` | `python check.py 2 cinema_ticket` |

Check the whole week at once: `python check.py 2`

## Project: Choose-your-own-adventure

A short text adventure where the player's choices lead to different endings.

Run it with `python weeks/week02_making_decisions/project.py`

- [ ] Write an opening scene and ask the player to choose (A or B)
- [ ] Use if / elif / else to send them down different paths
- [ ] Add a second choice inside at least one path (an if inside an if)
- [ ] Write at least 3 different endings
- [ ] Handle typos: tell the player when they type something unexpected
- [ ] Use .lower() so “A” and “a” both work

**Stretch goal:** Add a health or gold variable that changes with each choice and decides the ending.
