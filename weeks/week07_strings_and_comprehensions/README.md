# Week 7: Strings and comprehensions

Shape text like a pro, and write loops in a single line.

**Goals:** String methods · split and join · List comprehensions · Dict comprehensions

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_title_case.py` | `python check.py 7 title_case` |
| `ex2_squares_of_evens.py` | `python check.py 7 squares_of_evens` |
| `ex3_acronym_maker.py` | `python check.py 7 acronym_maker` |
| `ex4_caesar_cipher.py` | `python check.py 7 caesar_cipher` |
| `ex5_word_lengths.py` | `python check.py 7 word_lengths` |

Check the whole week at once: `python check.py 7`

## Project: Password toolkit

A program that checks how strong a password is and can generate strong new ones.

Run it with `python weeks/week07_strings_and_comprehensions/project.py`

- [ ] Write check_strength(pw) that scores length, digits, upper case, lower case and symbols
- [ ] Print a rating (weak / okay / strong) with tips on what's missing
- [ ] Write generate(length) using random.choice on a string of allowed characters
- [ ] Make sure generated passwords always include at least one of each type
- [ ] Add a menu: check / generate / quit

**Stretch goal:** Generate memorable passphrases from a list of words, like “tiger-lamp-river-42”.
