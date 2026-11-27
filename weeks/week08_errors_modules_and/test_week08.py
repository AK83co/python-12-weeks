# Automatic tests for week 8: Errors, modules and debugging
# Run them with:  python check.py 8
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


# ---- Exercise 1: Safe division ----
from ex1_safe_division import *  # noqa


def test_safe_division_1():
    assert (safe_divide(10, 2)) == (5.0)


def test_safe_division_2():
    assert (safe_divide(1, 0)) == (None)


def test_safe_division_3():
    assert (safe_divide(-9, 3)) == (-3.0)


# ---- Exercise 2: Forgiving number reader ----
from ex2_forgiving_number_reader import *  # noqa


def test_forgiving_number_reader_1():
    assert (to_int("42")) == (42)


def test_forgiving_number_reader_2():
    assert (to_int("abc")) == (0)


def test_forgiving_number_reader_3():
    assert (to_int("abc", -1)) == (-1)


def test_forgiving_number_reader_4():
    assert (to_int(" 7 ")) == (7)


def test_forgiving_number_reader_5():
    assert (to_int("3.5")) == (0)


# ---- Exercise 3: Validate an age ----
from ex3_validate_an_age import *  # noqa


def test_validate_an_age_1():
    assert (validate_age(30)) == (30)


def test_validate_an_age_2():
    assert (validate_age(0)) == (0)


def test_validate_an_age_3():
    assert (__raises(lambda: validate_age(-1), ValueError)) == (True)


def test_validate_an_age_4():
    assert (__raises(lambda: validate_age(200), ValueError)) == (True)


# ---- Exercise 4: Hypotenuse ----
from ex4_hypotenuse import *  # noqa


def test_hypotenuse_1():
    assert (hypotenuse(3, 4)) == (5.0)


def test_hypotenuse_2():
    assert (hypotenuse(1, 1)) == (1.41)


def test_hypotenuse_3():
    assert (hypotenuse(5, 12)) == (13.0)
