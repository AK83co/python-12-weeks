# Automatic tests for week 3: Loops
# Run them with:  python check.py 3
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


# ---- Exercise 1: Add them up ----
from ex1_add_them_up import *  # noqa


def test_add_them_up_1():
    assert (sum_to(3)) == (6)


def test_add_them_up_2():
    assert (sum_to(10)) == (55)


def test_add_them_up_3():
    assert (sum_to(100)) == (5050)


def test_add_them_up_4():
    assert (sum_to(0)) == (0)


# ---- Exercise 2: Count the vowels ----
from ex2_count_the_vowels import *  # noqa


def test_count_the_vowels_1():
    assert (count_vowels("hello")) == (2)


def test_count_the_vowels_2():
    assert (count_vowels("PYTHON")) == (1)


def test_count_the_vowels_3():
    assert (count_vowels("xyz")) == (0)


def test_count_the_vowels_4():
    assert (count_vowels("AEIOU aeiou")) == (10)


# ---- Exercise 3: FizzBuzz ----
def test_fizzbuzz():
    expected = "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"
    assert run_output("ex3_fizzbuzz.py") == expected


# ---- Exercise 4: Reverse it ----
from ex4_reverse_it import *  # noqa


def test_reverse_it_1():
    assert (reverse("hello")) == ("olleh")


def test_reverse_it_2():
    assert (reverse("Python")) == ("nohtyP")


def test_reverse_it_3():
    assert (reverse("a")) == ("a")


def test_reverse_it_4():
    assert (reverse("")) == ("")


# ---- Exercise 5: Power of two ----
from ex5_power_of_two import *  # noqa


def test_power_of_two_1():
    assert (next_power_of_two(1)) == (1)


def test_power_of_two_2():
    assert (next_power_of_two(5)) == (8)


def test_power_of_two_3():
    assert (next_power_of_two(64)) == (64)


def test_power_of_two_4():
    assert (next_power_of_two(100)) == (128)
