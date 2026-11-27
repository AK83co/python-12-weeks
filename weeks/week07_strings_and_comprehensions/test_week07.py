# Automatic tests for week 7: Strings and comprehensions
# Run them with:  python check.py 7
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


# ---- Exercise 1: Title Case ----
load("ex1_title_case.py")


def test_title_case_1():
    assert (title_case("hello world")) == ("Hello World")


def test_title_case_2():
    assert (title_case("the QUICK brown")) == ("The Quick Brown")


def test_title_case_3():
    assert (title_case("a")) == ("A")


def test_title_case_4():
    assert (title_case("learn python fast")) == ("Learn Python Fast")


# ---- Exercise 2: Squares of evens ----
load("ex2_squares_of_evens.py")


def test_squares_of_evens_1():
    assert (squares_of_evens([1, 2, 3, 4])) == ([4, 16])


def test_squares_of_evens_2():
    assert (squares_of_evens([1, 3, 5])) == ([])


def test_squares_of_evens_3():
    assert (squares_of_evens([10, -2])) == ([100, 4])


# ---- Exercise 3: Acronym maker ----
load("ex3_acronym_maker.py")


def test_acronym_maker_1():
    assert (acronym("portable network graphics")) == ("PNG")


def test_acronym_maker_2():
    assert (acronym("as soon as possible")) == ("ASAP")


def test_acronym_maker_3():
    assert (acronym("Python")) == ("P")


# ---- Exercise 4: Caesar cipher ----
load("ex4_caesar_cipher.py")


def test_caesar_cipher_1():
    assert (caesar("abc", 1)) == ("bcd")


def test_caesar_cipher_2():
    assert (caesar("xyz", 3)) == ("abc")


def test_caesar_cipher_3():
    assert (caesar("Hello, World!", 5)) == ("Mjqqt, Btwqi!")


def test_caesar_cipher_4():
    assert (caesar("Mjqqt", 21)) == ("Hello")


# ---- Exercise 5: Word lengths ----
load("ex5_word_lengths.py")


def test_word_lengths_1():
    assert (word_lengths("I love Python!")) == ({"i": 1, "love": 4, "python": 6})


def test_word_lengths_2():
    assert (word_lengths("Hi, there.")) == ({"hi": 2, "there": 5})
