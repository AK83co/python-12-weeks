# Automatic tests for week 1: Hello, Python
# Run them with:  python check.py 1
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


# ---- Exercise 1: Hello, World! ----
def test_hello_world():
    expected = "Hello, World!"
    assert run_output("ex1_hello_world.py") == expected


# ---- Exercise 2: About me ----
def test_about_me():
    expected = "Name: Ada\nAge: 36\nAda will be 46 in ten years."
    assert run_output("ex2_about_me.py") == expected


# ---- Exercise 3: Make a greeting ----
load("ex3_make_a_greeting.py")


def test_make_a_greeting_1():
    assert (make_greeting("Ada", "London")) == ("Hi Ada from London!")


def test_make_a_greeting_2():
    assert (make_greeting("Sam", "Lagos")) == ("Hi Sam from Lagos!")


def test_make_a_greeting_3():
    assert (make_greeting("Mia", "Tokyo")) == ("Hi Mia from Tokyo!")


# ---- Exercise 4: Seconds in some days ----
load("ex4_seconds_in_some_days.py")


def test_seconds_in_some_days_1():
    assert (days_to_seconds(1)) == (86400)


def test_seconds_in_some_days_2():
    assert (days_to_seconds(2)) == (172800)


def test_seconds_in_some_days_3():
    assert (days_to_seconds(0)) == (0)


def test_seconds_in_some_days_4():
    assert (days_to_seconds(7)) == (604800)


# ---- Exercise 5: Initials ----
load("ex5_initials.py")


def test_initials_1():
    assert (initials("Ada", "Lovelace")) == ("A.L.")


def test_initials_2():
    assert (initials("grace", "hopper")) == ("G.H.")


def test_initials_3():
    assert (initials("alan", "Turing")) == ("A.T.")
