# Automatic tests for week 10: Inheritance and special methods
# Run them with:  python check.py 10
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


# ---- Exercise 1: Animal sounds ----
load("ex1_animal_sounds.py")


def test_animal_sounds_1():
    assert (Dog("Rex").speak()) == ("Woof")


def test_animal_sounds_2():
    assert (Cow("Daisy").describe()) == ("Daisy says Moo")


def test_animal_sounds_3():
    assert (isinstance(Dog("x"), Animal)) == (True)


# ---- Exercise 2: 2D vectors ----
load("ex2_2d_vectors.py")


def test_2d_vectors_1():
    assert (Vector(1, 2) + Vector(3, 4) == Vector(4, 6)) == (True)


def test_2d_vectors_2():
    assert (Vector(1, 1) == Vector(1, 2)) == (False)


def test_2d_vectors_3():
    assert (repr(Vector(3, -1))) == ("Vector(3, -1)")


# ---- Exercise 3: Playlist ----
load("ex3_playlist.py")

def __check_playlist():
    p = Playlist()
    p.add(("Song A", 3))
    p.add(("Song B", 4))
    return [len(p), p.total_minutes()]


def test_playlist_1():
    assert (__check_playlist()) == ([2, 7])


def test_playlist_2():
    assert (len(Playlist())) == (0)


# ---- Exercise 4: Shapes ----
load("ex4_shapes.py")


def test_shapes_1():
    assert (Square(3).area()) == (9)


def test_shapes_2():
    assert (Circle(1).area()) == (3.14)


def test_shapes_3():
    assert (Circle(2).area()) == (12.57)


def test_shapes_4():
    assert (isinstance(Circle(1), Shape)) == (True)
