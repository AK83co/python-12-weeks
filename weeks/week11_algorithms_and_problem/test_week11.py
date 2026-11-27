# Automatic tests for week 11: Algorithms and problem solving
# Run them with:  python check.py 11
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


# ---- Exercise 1: Recursive factorial ----
load("ex1_recursive_factorial.py")


def test_recursive_factorial_1():
    assert (factorial(0)) == (1)


def test_recursive_factorial_2():
    assert (factorial(1)) == (1)


def test_recursive_factorial_3():
    assert (factorial(5)) == (120)


def test_recursive_factorial_4():
    assert (factorial(10)) == (3628800)


# ---- Exercise 2: Binary search ----
load("ex2_binary_search.py")


def test_binary_search_1():
    assert (binary_search([1, 3, 5, 7, 9], 7)) == (3)


def test_binary_search_2():
    assert (binary_search([1, 3, 5, 7, 9], 4)) == (-1)


def test_binary_search_3():
    assert (binary_search([1, 3, 5, 7, 9], 1)) == (0)


def test_binary_search_4():
    assert (binary_search([1, 3, 5, 7, 9], 9)) == (4)


def test_binary_search_5():
    assert (binary_search([], 5)) == (-1)


def test_binary_search_6():
    assert (binary_search(list(range(0, 100000, 2)), 77778)) == (38889)


# ---- Exercise 3: Fast Fibonacci ----
load("ex3_fast_fibonacci.py")


def test_fast_fibonacci_1():
    assert (fib(0)) == (0)


def test_fast_fibonacci_2():
    assert (fib(1)) == (1)


def test_fast_fibonacci_3():
    assert (fib(10)) == (55)


def test_fast_fibonacci_4():
    assert (fib(30)) == (832040)


def test_fast_fibonacci_5():
    assert (fib(80)) == (23416728348467685)


# ---- Exercise 4: Flatten ----
load("ex4_flatten.py")


def test_flatten_1():
    assert (flatten([1, [2, [3, [4]]], 5])) == ([1, 2, 3, 4, 5])


def test_flatten_2():
    assert (flatten([[], [[]]])) == ([])


def test_flatten_3():
    assert (flatten([1, 2, 3])) == ([1, 2, 3])


def test_flatten_4():
    assert (flatten([["a"], ["b", ["c"]]])) == (["a", "b", "c"])


# ---- Exercise 5: Balanced brackets ----
load("ex5_balanced_brackets.py")


def test_balanced_brackets_1():
    assert (is_balanced("([]{})")) == (True)


def test_balanced_brackets_2():
    assert (is_balanced("([)]")) == (False)


def test_balanced_brackets_3():
    assert (is_balanced("print(x[0])")) == (True)


def test_balanced_brackets_4():
    assert (is_balanced("((")) == (False)


def test_balanced_brackets_5():
    assert (is_balanced("}")) == (False)


def test_balanced_brackets_6():
    assert (is_balanced("")) == (True)
