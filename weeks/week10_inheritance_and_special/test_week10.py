# Automatic tests for week 10: Inheritance and special methods
# Run them with:  python check.py 10
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


# ---- Exercise 1: Animal sounds ----
from ex1_animal_sounds import *  # noqa


def test_animal_sounds_1():
    assert (Dog("Rex").speak()) == ("Woof")


def test_animal_sounds_2():
    assert (Cow("Daisy").describe()) == ("Daisy says Moo")


def test_animal_sounds_3():
    assert (isinstance(Dog("x"), Animal)) == (True)


# ---- Exercise 2: 2D vectors ----
from ex2_2d_vectors import *  # noqa


def test_2d_vectors_1():
    assert (Vector(1, 2) + Vector(3, 4) == Vector(4, 6)) == (True)


def test_2d_vectors_2():
    assert (Vector(1, 1) == Vector(1, 2)) == (False)


def test_2d_vectors_3():
    assert (repr(Vector(3, -1))) == ("Vector(3, -1)")


# ---- Exercise 3: Playlist ----
from ex3_playlist import *  # noqa

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
from ex4_shapes import *  # noqa


def test_shapes_1():
    assert (Square(3).area()) == (9)


def test_shapes_2():
    assert (Circle(1).area()) == (3.14)


def test_shapes_3():
    assert (Circle(2).area()) == (12.57)


def test_shapes_4():
    assert (isinstance(Circle(1), Shape)) == (True)
