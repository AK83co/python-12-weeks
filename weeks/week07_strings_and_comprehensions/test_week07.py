# Automatic tests for week 7: Strings and comprehensions
# Run them with:  python check.py 7
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


# ---- Exercise 1: Title Case ----
from ex1_title_case import *  # noqa


def test_title_case_1():
    assert (title_case("hello world")) == ("Hello World")


def test_title_case_2():
    assert (title_case("the QUICK brown")) == ("The Quick Brown")


def test_title_case_3():
    assert (title_case("a")) == ("A")


def test_title_case_4():
    assert (title_case("learn python fast")) == ("Learn Python Fast")


# ---- Exercise 2: Squares of evens ----
from ex2_squares_of_evens import *  # noqa


def test_squares_of_evens_1():
    assert (squares_of_evens([1, 2, 3, 4])) == ([4, 16])


def test_squares_of_evens_2():
    assert (squares_of_evens([1, 3, 5])) == ([])


def test_squares_of_evens_3():
    assert (squares_of_evens([10, -2])) == ([100, 4])


# ---- Exercise 3: Acronym maker ----
from ex3_acronym_maker import *  # noqa


def test_acronym_maker_1():
    assert (acronym("portable network graphics")) == ("PNG")


def test_acronym_maker_2():
    assert (acronym("as soon as possible")) == ("ASAP")


def test_acronym_maker_3():
    assert (acronym("Python")) == ("P")


# ---- Exercise 4: Caesar cipher ----
from ex4_caesar_cipher import *  # noqa


def test_caesar_cipher_1():
    assert (caesar("abc", 1)) == ("bcd")


def test_caesar_cipher_2():
    assert (caesar("xyz", 3)) == ("abc")


def test_caesar_cipher_3():
    assert (caesar("Hello, World!", 5)) == ("Mjqqt, Btwqi!")


def test_caesar_cipher_4():
    assert (caesar("Mjqqt", 21)) == ("Hello")


# ---- Exercise 5: Word lengths ----
from ex5_word_lengths import *  # noqa


def test_word_lengths_1():
    assert (word_lengths("I love Python!")) == ({"i": 1, "love": 4, "python": 6})


def test_word_lengths_2():
    assert (word_lengths("Hi, there.")) == ({"hi": 2, "there": 5})
