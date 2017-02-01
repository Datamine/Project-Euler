# Project-Euler
My solutions to Project Euler exercises. Currently this lists only Python3 solutions,
but I plan to add some solutions in other languages as well.

- `new-problem.py`: running this generates a new folder and solution template. 
Takes one command-line argument: the new problem. Example: `python3 new-problem.py 999`.

All solutions should be run from the `/Project-Euler` directory. There's a small
preamble in some solutions that appends to the system path so that `Utilities` can
be imported. For example, from here you might run: `python3 005/solution.py`.

## Addenda

Also included are some test-suites, etc. You may find the following files useful:

- `clean-swapfiles.sh`: recursively cleans out all the vim swapfiles in the directory.
Remember to `chmod 755 clean-swapfiles.sh` before attempting to use.

- `tests.py`: runs all the tests in the `Tests` directory, with verbose output.
Call with `python3 tests.py`. 

- `Tests`: directory containing unittests for the Utilities. Call with e.g. `python3 Tests/math_helpers_test.py`.

- `confirm-solutions.py`: runs all the solutions files currently in the `Problems` subdirectories.
Verifies the solutions against the canonical values. This is useful to check that all solutions
are still working as desired, even after having made some changes to the `Utilities`.
Run simply with `python3 confirm-solutions.py`.

## Further Notes

There's no `requirements.txt` because this project solely uses standard, included libraries
and the custom-written `Utilities`. 
