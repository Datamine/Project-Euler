#!/usr/bin/python3
"""
script to run all solutions in the Problems/ directory, and to confirm that the
solutions output is equal to the canonical values. This is to ensure that solutions
don't break after adjusting helper functions, for example.
"""

import os
import importlib

# solutions dict for Euler Problems thus far
solutions = {
    "001": 233168,
    "002": 4613732,
    "003": 6857,
    "004": 906609,
    "005": 232792560,
    "006": 25164150,
    "007": 104743,
    "008": 23514624000,
    "009": 31875000,
    "010": 142913828922,
    "011": 70600674,
    "012": 76576500,
}

# lambda filter to remove the __pycache__ dir, __init__ file from consideration
problems = sorted(filter(lambda x: x.isdigit(), os.listdir("Problems")))
for problem_number in problems:
    path = os.path.join("Problems", problem_number, "solution")
    path_package_formatted = path.replace("/", ".")
    try:
        current_sol = importlib.import_module(path_package_formatted)
        solution_obtained = current_sol.main()
        if solutions[problem_number] == solution_obtained:
            print("Problem {}: MATCH.".format(problem_number))
        else:
            print("Problem {}: ERROR. Expected: {}, Received: {}".format(problem_number, solutions[problem_number], solution_obtained))
    except Exception as e:
        # note: using just 'e' is not always sufficient, e.g. for KeyErrors, it
        # just writes the key, not the helpful word "KeyError".
        # e.message would be helpful, but that's deprecated since Python 2.6.
        print("Problem {}: EXCEPTION. {}".format(problem_number, e))
