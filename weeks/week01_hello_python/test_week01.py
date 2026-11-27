# Automatic tests for week 1: Hello, Python
# Run them with:  python check.py 1
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


# ---- Exercise 1: Hello, World! ----
def test_hello_world():
    expected = "Hello, World!"
    assert run_output("ex1_hello_world.py") == expected


# ---- Exercise 2: About me ----
def test_about_me():
    expected = "Name: Ada\nAge: 36\nAda will be 46 in ten years."
    assert run_output("ex2_about_me.py") == expected


# ---- Exercise 3: Make a greeting ----
from ex3_make_a_greeting import *  # noqa


def test_make_a_greeting_1():
    assert (make_greeting("Ada", "London")) == ("Hi Ada from London!")


def test_make_a_greeting_2():
    assert (make_greeting("Sam", "Lagos")) == ("Hi Sam from Lagos!")


def test_make_a_greeting_3():
    assert (make_greeting("Mia", "Tokyo")) == ("Hi Mia from Tokyo!")


# ---- Exercise 4: Seconds in some days ----
from ex4_seconds_in_some_days import *  # noqa


def test_seconds_in_some_days_1():
    assert (days_to_seconds(1)) == (86400)


def test_seconds_in_some_days_2():
    assert (days_to_seconds(2)) == (172800)


def test_seconds_in_some_days_3():
    assert (days_to_seconds(0)) == (0)


def test_seconds_in_some_days_4():
    assert (days_to_seconds(7)) == (604800)


# ---- Exercise 5: Initials ----
from ex5_initials import *  # noqa


def test_initials_1():
    assert (initials("Ada", "Lovelace")) == ("A.L.")


def test_initials_2():
    assert (initials("grace", "hopper")) == ("G.H.")


def test_initials_3():
    assert (initials("alan", "Turing")) == ("A.T.")
