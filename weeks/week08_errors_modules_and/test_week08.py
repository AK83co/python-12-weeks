# Automatic tests for week 8: Errors, modules and debugging
# Run them with:  python check.py 8
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


# ---- Exercise 1: Safe division ----
load("ex1_safe_division.py")


def test_safe_division_1():
    assert (safe_divide(10, 2)) == (5.0)


def test_safe_division_2():
    assert (safe_divide(1, 0)) == (None)


def test_safe_division_3():
    assert (safe_divide(-9, 3)) == (-3.0)


# ---- Exercise 2: Forgiving number reader ----
load("ex2_forgiving_number_reader.py")


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
load("ex3_validate_an_age.py")


def test_validate_an_age_1():
    assert (validate_age(30)) == (30)


def test_validate_an_age_2():
    assert (validate_age(0)) == (0)


def test_validate_an_age_3():
    assert (__raises(lambda: validate_age(-1), ValueError)) == (True)


def test_validate_an_age_4():
    assert (__raises(lambda: validate_age(200), ValueError)) == (True)


# ---- Exercise 4: Hypotenuse ----
load("ex4_hypotenuse.py")


def test_hypotenuse_1():
    assert (hypotenuse(3, 4)) == (5.0)


def test_hypotenuse_2():
    assert (hypotenuse(1, 1)) == (1.41)


def test_hypotenuse_3():
    assert (hypotenuse(5, 12)) == (13.0)
