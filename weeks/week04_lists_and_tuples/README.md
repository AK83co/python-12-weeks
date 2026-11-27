# Week 4: Lists and tuples

Store many values in one place and work with them all at once.

**Goals:** Create and index lists · Slice · List methods · Tuples and unpacking

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_find_the_biggest.py` | `python check.py 4 find_the_biggest` |
| `ex2_average.py` | `python check.py 4 average` |
| `ex3_remove_duplicates.py` | `python check.py 4 remove_duplicates` |
| `ex4_second_largest.py` | `python check.py 4 second_largest` |
| `ex5_rotate_a_list.py` | `python check.py 4 rotate_a_list` |

Check the whole week at once: `python check.py 4`

## Project: Terminal to-do list

A menu-driven to-do app: add tasks, show them, tick them off, and quit. Month 1 capstone!

Run it with `python weeks/week04_lists_and_tuples/project.py`

- [ ] Show a menu in a loop: add / show / done / quit
- [ ] Add tasks to a list
- [ ] Show tasks numbered from 1 (use enumerate)
- [ ] Mark a task done by its number (remove it, or move it to a done list)
- [ ] Handle bad input, like a number that isn't in the list
- [ ] Show how many tasks are left

**Stretch goal:** Add priorities (high/low) stored as tuples like ("buy milk", "high") and show high-priority tasks first.
