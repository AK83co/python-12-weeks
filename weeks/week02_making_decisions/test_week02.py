# Automatic tests for week 2: Making decisions
# Run them with:  python check.py 2
# You don't need to edit this file.

import builtins
import contextlib
import io
import subprocess
import sys
import warnings
from pathlib import Path

HERE = Path(__file__).parent


class _StopExtraCode(Exception):
    pass


def load(filename):
    """Run an exercise file and give the tests its functions and classes.

    You can add your own code below your function, even code that uses
    input() or print(). While testing, input() gets the answer "1" and
    anything printed is hidden, so your extra code can't break the tests.
    """
    namespace = {"__name__": "exercise"}  # so if __name__ == "__main__": blocks are skipped
    code = compile((HERE / filename).read_text(encoding="utf-8"), str(HERE / filename), "exec")
    calls = 0

    def fake_input(prompt=""):
        nonlocal calls
        calls += 1
        if calls > 100:
            raise _StopExtraCode()  # a loop that keeps asking forever
        return "1"

    real_input = builtins.input
    builtins.input = fake_input
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(code, namespace)
    except _StopExtraCode:
        pass
    except Exception as error:
        warnings.warn(f"{filename}: your extra code crashed while testing ({type(error).__name__}: {error}). The tests still checked everything defined above that line.")
    finally:
        builtins.input = real_input
    globals().update({k: v for k, v in namespace.items() if not k.startswith("__")})


def __raises(f, exc):
    try:
        f()
    except exc:
        return True
    except Exception:
        return False
    return False


def run_output(filename):
    result = subprocess.run([sys.executable, str(HERE / filename)], capture_output=True, text=True, input="1\n" * 20, timeout=10)
    assert result.returncode == 0, result.stderr
    return "\n".join(line.rstrip() for line in result.stdout.strip().splitlines())


# ---- Exercise 1: Even or odd ----
load("ex1_even_or_odd.py")


def test_even_or_odd_1():
    assert (is_even(4)) == (True)


def test_even_or_odd_2():
    assert (is_even(7)) == (False)


def test_even_or_odd_3():
    assert (is_even(0)) == (True)


def test_even_or_odd_4():
    assert (is_even(-3)) == (False)


# ---- Exercise 2: Letter grade ----
load("ex2_letter_grade.py")


def test_letter_grade_1():
    assert (grade(95)) == ("A")


def test_letter_grade_2():
    assert (grade(90)) == ("A")


def test_letter_grade_3():
    assert (grade(85)) == ("B")


def test_letter_grade_4():
    assert (grade(72)) == ("C")


def test_letter_grade_5():
    assert (grade(60)) == ("D")


def test_letter_grade_6():
    assert (grade(40)) == ("F")


# ---- Exercise 3: Biggest of three ----
load("ex3_biggest_of_three.py")


def test_biggest_of_three_1():
    assert (max_of_three(3, 9, 2)) == (9)


def test_biggest_of_three_2():
    assert (max_of_three(10, 4, 7)) == (10)


def test_biggest_of_three_3():
    assert (max_of_three(1, 2, 3)) == (3)


def test_biggest_of_three_4():
    assert (max_of_three(-1, -5, -2)) == (-1)


def test_biggest_of_three_5():
    assert (max_of_three(5, 5, 5)) == (5)


# ---- Exercise 4: Leap year ----
load("ex4_leap_year.py")


def test_leap_year_1():
    assert (is_leap(2024)) == (True)


def test_leap_year_2():
    assert (is_leap(2023)) == (False)


def test_leap_year_3():
    assert (is_leap(1900)) == (False)


def test_leap_year_4():
    assert (is_leap(2000)) == (True)


def test_leap_year_5():
    assert (is_leap(2026)) == (False)


# ---- Exercise 5: Cinema ticket ----
load("ex5_cinema_ticket.py")


def test_cinema_ticket_1():
    assert (ticket_price(3)) == (0)


def test_cinema_ticket_2():
    assert (ticket_price(5)) == (8)


def test_cinema_ticket_3():
    assert (ticket_price(17)) == (8)


def test_cinema_ticket_4():
    assert (ticket_price(18)) == (12)


def test_cinema_ticket_5():
    assert (ticket_price(64)) == (12)


def test_cinema_ticket_6():
    assert (ticket_price(65)) == (6)
