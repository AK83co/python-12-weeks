"""
Week 7 · Exercise 4: Caesar cipher

Write caesar(text, shift) that shifts each letter forward in the alphabet by
shift, wrapping around from z to a. Keep upper/lower case, and leave
anything that isn't a letter unchanged.

Examples:
    caesar("abc", 1)            →  "bcd"
    caesar("xyz", 3)            →  "abc"
    caesar("Hello, World!", 5)  →  "Mjqqt, Btwqi!"

Check your answer:  python check.py 7 caesar_cipher
"""

def caesar(text, shift):
    result = ""
    for ch in text:
        # shift letters, keep everything else
        result += ch
    return result
