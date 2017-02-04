# Project-Euler
My solutions to Project Euler exercises. Currently this lists only solutions in Python 3.6,
though I may eventually add some solutions in other languages as well.

All solutions should be run from the `/Project-Euler` directory. There's a small
preamble in some solutions that appends to the system path so that `Utilities` can
be imported. For example, from here you might run: `python3 005/solution.py`.

## Tools and Addenda

You may find the following useful:

- `new-problem.py`: running this generates a new folder and solution template. 
Takes one command-line argument: the new problem. Example: `python3 new-problem.py 999`.

- `clean-swapfiles.sh`: recursively cleans out all the vim swapfiles in the directory.
Remember to `chmod 755 clean-swapfiles.sh` before attempting to use.

- `tests.py`: runs all the tests in the `Tests` directory, with verbose output.
Call with `python3 tests.py`. 

- `Tests`: directory containing unittests for the Utilities. Call with e.g. `python3 Tests/math_helpers_test.py`.

- `Utilities`: directory containing modules containing frequently used/re-usable helper functions.

- `confirm-solutions.py`: runs all the solutions files currently in the `Problems` subdirectories.
Verifies the solutions against the canonical values. This is useful to check that all solutions
are still working as desired, even after having made some changes to the `Utilities`.
Run simply with `python3 confirm-solutions.py`.

## Further Notes

There's no `requirements.txt` because this project solely uses the standard modules that are included
with any conventional installation of Python 3.6, as well as the custom-written `Utilities`. 

I've also featured this project on my blog, where I [wrote a little bit about it](https://github.com/Datamine/Project-Euler).
