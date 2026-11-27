# Week 5 project: Calculator
#
# A command-line calculator built from small functions, one per operation.
#
# Milestones:
#   1. Write add, subtract, multiply and divide functions that each return a value
#   2. Make divide return an error message when dividing by zero
#   3. Build a menu loop that asks for two numbers and an operation
#   4. Call the right function and print the result
#   5. Add power and square root (import math)
#   6. Keep a history list of past calculations and add a 'history' command
#
# Run it:  python weeks/week05_functions/project.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero"
    return a / b

while True:
    op = input("Operation (+, /, q to quit): ")
    if op == "q":
        break
    a = float(input("First number: "))
    b = float(input("Second number: "))
    if op == "+":
        print("=", add(a, b))
    elif op == "/":
        print("=", divide(a, b))
