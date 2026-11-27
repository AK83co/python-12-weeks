# Automatic tests for week 5: Functions
# Run them with:  python check.py 5
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


# ---- Exercise 1: Power with a default ----
from ex1_power_with_a_default import *  # noqa


def test_power_with_a_default_1():
    assert (power(5)) == (25)


def test_power_with_a_default_2():
    assert (power(2, 10)) == (1024)


def test_power_with_a_default_3():
    assert (power(3, 3)) == (27)


def test_power_with_a_default_4():
    assert (power(exp=0, base=9)) == (1)


# ---- Exercise 2: Temperature converter ----
from ex2_temperature_converter import *  # noqa


def test_temperature_converter_1():
    assert (c_to_f(0)) == (32.0)


def test_temperature_converter_2():
    assert (c_to_f(100)) == (212.0)


def test_temperature_converter_3():
    assert (c_to_f(37.5)) == (99.5)


def test_temperature_converter_4():
    assert (c_to_f(-40)) == (-40.0)


def test_temperature_converter_5():
    assert (c_to_f(21)) == (69.8)


# ---- Exercise 3: Palindrome ----
from ex3_palindrome import *  # noqa


def test_palindrome_1():
    assert (is_palindrome("Racecar")) == (True)


def test_palindrome_2():
    assert (is_palindrome("A man, a plan, a canal: Panama")) == (True)


def test_palindrome_3():
    assert (is_palindrome("hello")) == (False)


def test_palindrome_4():
    assert (is_palindrome("Was it a car or a cat I saw?")) == (True)


# ---- Exercise 4: Min and max together ----
from ex4_min_and_max_together import *  # noqa


def test_min_and_max_together_1():
    assert (min_max([3, 1, 4, 1, 5])) == ((1, 5))


def test_min_and_max_together_2():
    assert (min_max([7])) == ((7, 7))


def test_min_and_max_together_3():
    assert (min_max([-2, -9, 0])) == ((-9, 0))


# ---- Exercise 5: Shopping discount ----
from ex5_shopping_discount import *  # noqa


def test_shopping_discount_1():
    assert (apply_discount(50)) == (45.0)


def test_shopping_discount_2():
    assert (apply_discount(80, 25)) == (60.0)


def test_shopping_discount_3():
    assert (apply_discount(19.99, 15)) == (16.99)


def test_shopping_discount_4():
    assert (apply_discount(30, 150)) == (30)


def test_shopping_discount_5():
    assert (apply_discount(30, -5)) == (30)
