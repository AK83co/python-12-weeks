# Week 9: Classes and objects

Model real things in code with your own types.

**Goals:** Define a class · __init__ and self · Methods · __str__

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_rectangle.py` | `python check.py 9 rectangle` |
| `ex2_bank_account.py` | `python check.py 9 bank_account` |
| `ex3_student_report.py` | `python check.py 9 student_report` |
| `ex4_print_a_playing_card.py` | `python check.py 9 print_a_playing_card` |

Check the whole week at once: `python check.py 9`

## Project: Virtual pet

Create a pet that gets hungry and bored over time. Feed it and play with it to keep it happy.

Run it with `python weeks/week09_classes_and_objects/project.py`

- [ ] Write a Pet class with name, hunger and happiness attributes
- [ ] Add feed(), play() and status() methods
- [ ] Add a tick() method that makes the pet hungrier and less happy each turn
- [ ] Build a game loop: each turn, show status and ask what to do
- [ ] End the game if hunger or happiness reaches a limit
- [ ] Add __str__ so print(pet) shows a little face like (^_^) or (T_T)

**Stretch goal:** Look after several pets at once by keeping a list of Pet objects.
