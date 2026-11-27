"""Check your exercises.

Usage (type these in the terminal at the bottom of the Codespace):
    python check.py 3            check every exercise in week 3
    python check.py 3 sum_to     check just one exercise
    python check.py all          check the whole course
"""
import glob
import subprocess
import sys

if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(0)

if sys.argv[1] == "all":
    target = "weeks"
else:
    try:
        week = int(sys.argv[1])
    except ValueError:
        print("Give a week number, like:  python check.py 3")
        sys.exit(1)
    folders = glob.glob(f"weeks/week{week:02d}_*")
    if not folders:
        print(f"There's no week {week}. Weeks go from 1 to 12.")
        sys.exit(1)
    target = folders[0]

args = [sys.executable, "-m", "pytest", target, "-q", "--no-header", "--tb=short", "-p", "no:cacheprovider", "--timeout=5"]
if len(sys.argv) > 2:
    args += ["-k", sys.argv[2]]
code = subprocess.call(args)
if code == 0:
    print("\nAll passed! Tick the exercise off on the course site.")
else:
    print("\nNot all passed yet. Read the first error above: 'assert X == Y' shows what you returned (X) and what was expected (Y).")
sys.exit(code)
