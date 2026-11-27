"""
Week 9 · Exercise 2: Bank account

Make a BankAccount class that starts with a balance. deposit(amount) adds
money. withdraw(amount) removes it and returns True, but if there isn't
enough money it returns False and leaves the balance alone.

Examples:
    acc = BankAccount(100)
    acc.deposit(50)
    acc.withdraw(30)   →  True
    acc.balance        →  120
    acc.withdraw(500)  →  False

Check your answer:  python check.py 9 bank_account
"""

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass
