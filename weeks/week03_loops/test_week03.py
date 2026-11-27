# Automatic tests for week 3: Loops
# Run them with:  python check.py 3
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


# ---- Exercise 1: Add them up ----
load("ex1_add_them_up.py")


def test_add_them_up_1():
    assert (sum_to(3)) == (6)


def test_add_them_up_2():
    assert (sum_to(10)) == (55)


def test_add_them_up_3():
    assert (sum_to(100)) == (5050)


def test_add_them_up_4():
    assert (sum_to(0)) == (0)


# ---- Exercise 2: Count the vowels ----
load("ex2_count_the_vowels.py")


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
load("ex4_reverse_it.py")


def test_reverse_it_1():
    assert (reverse("hello")) == ("olleh")


def test_reverse_it_2():
    assert (reverse("Python")) == ("nohtyP")


def test_reverse_it_3():
    assert (reverse("a")) == ("a")


def test_reverse_it_4():
    assert (reverse("")) == ("")


# ---- Exercise 5: Power of two ----
load("ex5_power_of_two.py")


def test_power_of_two_1():
    assert (next_power_of_two(1)) == (1)


def test_power_of_two_2():
    assert (next_power_of_two(5)) == (8)


def test_power_of_two_3():
    assert (next_power_of_two(64)) == (64)


def test_power_of_two_4():
    assert (next_power_of_two(100)) == (128)
