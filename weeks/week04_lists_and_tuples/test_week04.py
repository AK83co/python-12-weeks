# Automatic tests for week 4: Lists and tuples
# Run them with:  python check.py 4
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


# ---- Exercise 1: Find the biggest ----
from ex1_find_the_biggest import *  # noqa


def test_find_the_biggest_1():
    assert (largest([3, 9, 2])) == (9)


def test_find_the_biggest_2():
    assert (largest([-5, -2, -8])) == (-2)


def test_find_the_biggest_3():
    assert (largest([42])) == (42)


def test_find_the_biggest_4():
    assert (largest([1, 2, 3, 100, 4])) == (100)


# ---- Exercise 2: Average ----
from ex2_average import *  # noqa


def test_average_1():
    assert (average([1, 2, 3, 4])) == (2.5)


def test_average_2():
    assert (average([10, 20, 25])) == (18.33)


def test_average_3():
    assert (average([7])) == (7)


def test_average_4():
    assert (average([])) == (0)


# ---- Exercise 3: Remove duplicates ----
from ex3_remove_duplicates import *  # noqa


def test_remove_duplicates_1():
    assert (remove_duplicates([1, 2, 2, 3, 1])) == ([1, 2, 3])


def test_remove_duplicates_2():
    assert (remove_duplicates(["a", "b", "a"])) == (["a", "b"])


def test_remove_duplicates_3():
    assert (remove_duplicates([])) == ([])


def test_remove_duplicates_4():
    assert (remove_duplicates([5, 5, 5])) == ([5])


# ---- Exercise 4: Second largest ----
from ex4_second_largest import *  # noqa


def test_second_largest_1():
    assert (second_largest([4, 9, 2, 7])) == (7)


def test_second_largest_2():
    assert (second_largest([5, 5, 3])) == (3)


def test_second_largest_3():
    assert (second_largest([1, 2])) == (1)


def test_second_largest_4():
    assert (second_largest([10, 10, 9, 9, 8])) == (9)


# ---- Exercise 5: Rotate a list ----
from ex5_rotate_a_list import *  # noqa


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
