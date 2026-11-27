# Automatic tests for week 12: Real-world Python and your capstone
# Run them with:  python check.py 12
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


# ---- Exercise 1: Two Sum ----
load("ex1_two_sum.py")


def test_two_sum_1():
    assert (two_sum([2, 7, 11, 15], 9)) == ([0, 1])


def test_two_sum_2():
    assert (two_sum([3, 2, 4], 6)) == ([1, 2])


def test_two_sum_3():
    assert (two_sum([3, 3], 6)) == ([0, 1])


def test_two_sum_4():
    assert (two_sum([1, 5, 9, 14], 23)) == ([2, 3])


# ---- Exercise 2: Roman numerals ----
load("ex2_roman_numerals.py")


def test_roman_numerals_1():
    assert (to_roman(4)) == ("IV")


def test_roman_numerals_2():
    assert (to_roman(9)) == ("IX")


def test_roman_numerals_3():
    assert (to_roman(14)) == ("XIV")


def test_roman_numerals_4():
    assert (to_roman(1994)) == ("MCMXCIV")


def test_roman_numerals_5():
    assert (to_roman(2026)) == ("MMXXVI")


def test_roman_numerals_6():
    assert (to_roman(3999)) == ("MMMCMXCIX")


# ---- Exercise 3: Group by length ----
load("ex3_group_by_length.py")


def test_group_by_length_1():
    assert (group_by_length(["hi", "cat", "yo", "dog"])) == ({2: ["hi", "yo"], 3: ["cat", "dog"]})


def test_group_by_length_2():
    assert (group_by_length([])) == ({})


def test_group_by_length_3():
    assert (group_by_length(["python"])) == ({6: ["python"]})


# ---- Exercise 4: Merge sorted lists ----
load("ex4_merge_sorted_lists.py")


def test_merge_sorted_lists_1():
    assert (merge_sorted([1, 4, 9], [2, 3, 10])) == ([1, 2, 3, 4, 9, 10])


def test_merge_sorted_lists_2():
    assert (merge_sorted([], [1, 2])) == ([1, 2])


def test_merge_sorted_lists_3():
    assert (merge_sorted([5], [])) == ([5])


def test_merge_sorted_lists_4():
    assert (merge_sorted([1, 1], [1])) == ([1, 1, 1])
