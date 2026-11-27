# Automatic tests for week 9: Classes and objects
# Run them with:  python check.py 9
# You don't need to edit this file.

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent


def __raises(f, exc):
    try:
        f()
    except exc:
        return True
    except Exception:
        return False
    return False


def run_output(filename):
    result = subprocess.run([sys.executable, str(HERE / filename)], capture_output=True, text=True, input="", timeout=10)
    assert result.returncode == 0, result.stderr
    return "\n".join(line.rstrip() for line in result.stdout.strip().splitlines())


# ---- Exercise 1: Rectangle ----
from ex1_rectangle import *  # noqa


def test_rectangle_1():
    assert (Rectangle(3, 4).area()) == (12)


def test_rectangle_2():
    assert (Rectangle(3, 4).perimeter()) == (14)


def test_rectangle_3():
    assert (Rectangle(5, 5).area()) == (25)


def test_rectangle_4():
    assert (Rectangle(1, 10).perimeter()) == (22)


# ---- Exercise 2: Bank account ----
from ex2_bank_account import *  # noqa

def __check_bank():
    acc = BankAccount(100)
    acc.deposit(50)
    r1 = acc.withdraw(30)
    b1 = acc.balance
    r2 = acc.withdraw(500)
    return [r1, b1, r2, acc.balance]


def test_bank_account_1():
    assert (__check_bank()) == ([True, 120, False, 120])


def test_bank_account_2():
    assert (BankAccount().balance) == (0)


# ---- Exercise 3: Student report ----
from ex3_student_report import *  # noqa

def __check_student():
    s = Student("Ada")
    s.add_grade(90)
    s.add_grade(85)
    return [s.average(), s.name]


def test_student_report_1():
    assert (__check_student()) == ([87.5, 'Ada'])


def test_student_report_2():
    assert (Student("Bo").average()) == (0)


# ---- Exercise 4: Print a playing card ----
from ex4_print_a_playing_card import *  # noqa


def test_print_a_playing_card_1():
    assert (str(Card("Q", "hearts"))) == ("Q of hearts")


def test_print_a_playing_card_2():
    assert (str(Card("7", "spades"))) == ("7 of spades")


def test_print_a_playing_card_3():
    assert (Card("A", "clubs").suit) == ("clubs")
