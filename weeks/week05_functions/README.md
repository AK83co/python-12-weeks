# Week 5: Functions

Package your code into reusable, named tools.

**Goals:** def and return · Default and keyword arguments · Scope · Return several values

## Exercises

Open each file, write your code, then check it in the terminal:

| File | Check it with |
|---|---|
| `ex1_power_with_a_default.py` | `python check.py 5 power_with_a_default` |
| `ex2_temperature_converter.py` | `python check.py 5 temperature_converter` |
| `ex3_palindrome.py` | `python check.py 5 palindrome` |
| `ex4_min_and_max_together.py` | `python check.py 5 min_and_max_together` |
| `ex5_shopping_discount.py` | `python check.py 5 shopping_discount` |

Check the whole week at once: `python check.py 5`

## Project: Calculator

A command-line calculator built from small functions, one per operation.

Run it with `python weeks/week05_functions/project.py`

- [ ] Write add, subtract, multiply and divide functions that each return a value
- [ ] Make divide return an error message when dividing by zero
- [ ] Build a menu loop that asks for two numbers and an operation
- [ ] Call the right function and print the result
- [ ] Add power and square root (import math)
- [ ] Keep a history list of past calculations and add a 'history' command

**Stretch goal:** Let the user type a whole expression like 12 * 4 and split it into parts with .split().
