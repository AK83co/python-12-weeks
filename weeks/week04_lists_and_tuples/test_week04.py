# Automatic tests for week 4: Lists and tuples
# Run them with:  python check.py 4
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


# ---- Exercise 1: Find the biggest ----
load("ex1_find_the_biggest.py")


def test_find_the_biggest_1():
    assert (largest([3, 9, 2])) == (9)


def test_find_the_biggest_2():
    assert (largest([-5, -2, -8])) == (-2)


def test_find_the_biggest_3():
    assert (largest([42])) == (42)


def test_find_the_biggest_4():
    assert (largest([1, 2, 3, 100, 4])) == (100)


# ---- Exercise 2: Average ----
load("ex2_average.py")


def test_average_1():
    assert (average([1, 2, 3, 4])) == (2.5)


def test_average_2():
    assert (average([10, 20, 25])) == (18.33)


def test_average_3():
    assert (average([7])) == (7)


def test_average_4():
    assert (average([])) == (0)


# ---- Exercise 3: Remove duplicates ----
load("ex3_remove_duplicates.py")


def test_remove_duplicates_1():
    assert (remove_duplicates([1, 2, 2, 3, 1])) == ([1, 2, 3])


def test_remove_duplicates_2():
    assert (remove_duplicates(["a", "b", "a"])) == (["a", "b"])


def test_remove_duplicates_3():
    assert (remove_duplicates([])) == ([])


def test_remove_duplicates_4():
    assert (remove_duplicates([5, 5, 5])) == ([5])


# ---- Exercise 4: Second largest ----
load("ex4_second_largest.py")


def test_second_largest_1():
    assert (second_largest([4, 9, 2, 7])) == (7)


def test_second_largest_2():
    assert (second_largest([5, 5, 3])) == (3)


def test_second_largest_3():
    assert (second_largest([1, 2])) == (1)


def test_second_largest_4():
    assert (second_largest([10, 10, 9, 9, 8])) == (9)


# ---- Exercise 5: Rotate a list ----
load("ex5_rotate_a_list.py")


def test_rotate_a_list_1():
    assert (rotate([1, 2, 3, 4], 1)) == ([4, 1, 2, 3])


def test_rotate_a_list_2():
    assert (rotate([1, 2, 3, 4], 2)) == ([3, 4, 1, 2])


def test_rotate_a_list_3():
    assert (rotate([1, 2, 3, 4], 6)) == ([3, 4, 1, 2])


def test_rotate_a_list_4():
    assert (rotate([1, 2, 3], 0)) == ([1, 2, 3])


def test_rotate_a_list_5():
    assert (rotate([], 3)) == ([])
