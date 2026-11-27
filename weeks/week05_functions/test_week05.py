# Automatic tests for week 5: Functions
# Run them with:  python check.py 5
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


# ---- Exercise 1: Power with a default ----
load("ex1_power_with_a_default.py")


def test_power_with_a_default_1():
    assert (power(5)) == (25)


def test_power_with_a_default_2():
    assert (power(2, 10)) == (1024)


def test_power_with_a_default_3():
    assert (power(3, 3)) == (27)


def test_power_with_a_default_4():
    assert (power(exp=0, base=9)) == (1)


# ---- Exercise 2: Temperature converter ----
load("ex2_temperature_converter.py")


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
load("ex3_palindrome.py")


def test_palindrome_1():
    assert (is_palindrome("Racecar")) == (True)


def test_palindrome_2():
    assert (is_palindrome("A man, a plan, a canal: Panama")) == (True)


def test_palindrome_3():
    assert (is_palindrome("hello")) == (False)


def test_palindrome_4():
    assert (is_palindrome("Was it a car or a cat I saw?")) == (True)


# ---- Exercise 4: Min and max together ----
load("ex4_min_and_max_together.py")


def test_min_and_max_together_1():
    assert (min_max([3, 1, 4, 1, 5])) == ((1, 5))


def test_min_and_max_together_2():
    assert (min_max([7])) == ((7, 7))


def test_min_and_max_together_3():
    assert (min_max([-2, -9, 0])) == ((-9, 0))


# ---- Exercise 5: Shopping discount ----
load("ex5_shopping_discount.py")


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
