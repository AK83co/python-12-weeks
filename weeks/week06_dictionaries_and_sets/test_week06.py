# Automatic tests for week 6: Dictionaries and sets
# Run them with:  python check.py 6
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


# ---- Exercise 1: Word counter ----
load("ex1_word_counter.py")


def test_word_counter_1():
    assert (word_count("the cat the hat")) == ({"the": 2, "cat": 1, "hat": 1})


def test_word_counter_2():
    assert (word_count("Go go GO")) == ({"go": 3})


def test_word_counter_3():
    assert (word_count("one")) == ({"one": 1})


# ---- Exercise 2: Flip a dictionary ----
load("ex2_flip_a_dictionary.py")


def test_flip_a_dictionary_1():
    assert (invert({"a": 1, "b": 2})) == ({1: "a", 2: "b"})


def test_flip_a_dictionary_2():
    assert (invert({})) == ({})


def test_flip_a_dictionary_3():
    assert (invert({"red": "#f00", "blue": "#00f"})) == ({"#f00": "red", "#00f": "blue"})


# ---- Exercise 3: Things in common ----
load("ex3_things_in_common.py")


def test_things_in_common_1():
    assert (common([1, 2, 3, 4], [3, 4, 5])) == ([3, 4])


def test_things_in_common_2():
    assert (common([1, 1, 2], [1, 1])) == ([1])


def test_things_in_common_3():
    assert (common(["b", "a", "c"], ["c", "a"])) == (["a", "c"])


def test_things_in_common_4():
    assert (common([1, 2], [3])) == ([])


# ---- Exercise 4: Most common letter ----
load("ex4_most_common_letter.py")


def test_most_common_letter_1():
    assert (most_common_letter("hello")) == ("l")


def test_most_common_letter_2():
    assert (most_common_letter("Mississippi")) == ("i")


def test_most_common_letter_3():
    assert (most_common_letter("aabb")) == ("a")


def test_most_common_letter_4():
    assert (most_common_letter("Zebra zoo!")) == ("o")


# ---- Exercise 5: Shopping basket total ----
load("ex5_shopping_basket_total.py")


def test_shopping_basket_total_1():
    assert (basket_total({"apple": 3, "milk": 1}, {"apple": 0.5, "milk": 1.2})) == (2.7)


def test_shopping_basket_total_2():
    assert (basket_total({}, {"apple": 1})) == (0)


def test_shopping_basket_total_3():
    assert (basket_total({"gold": 2, "tea": 2}, {"tea": 3.25})) == (6.5)
