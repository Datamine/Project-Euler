#!/usr/bin/python3
"""
script to run all solutions in the Problems/ directory, and to confirm that the
solutions output is equal to the canonical values. This is to ensure that solutions
don't break after adjusting helper functions, for example.
"""

import os
import time
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
    "013": "5537376230",
    "014": 837799,
    "015": 137846528820,
    "016": 1366,
    "017": 21124,
    "018": 1074,
    "019": 171,
    "020": 648,
    "021": 31626,
    "022": 871198282,
    "023": 4179871,
    "024": "2783915460",
    "025": 4782,
    "026": 983,
    "027": -59231,
    "028": 669171001,
    "029": 9183,
    "030": 443839,
    "031": 73682,
    "032": 45228,
}

# lambda filter to remove the __pycache__ dir, __init__ file from consideration
problems = sorted(filter(lambda x: x.isdigit(), os.listdir("Problems")))
for problem_number in problems:
    path = os.path.join("Problems", problem_number, "solution")
    path_package_formatted = path.replace("/", ".")
    try:
        current_sol = importlib.import_module(path_package_formatted)
        start = time.time()
        solution_obtained = current_sol.main()
        time_elapsed = time.time() - start
        if solutions[problem_number] == solution_obtained:
            print("Problem {}: MATCH. Time: {:.5f}.\tSolution: {}.".format(problem_number, time_elapsed, solution_obtained))
        else:
            print("Problem {}: ERROR. Expected: {}, Received: {}".format(problem_number, solutions[problem_number], solution_obtained))
    except Exception as e:
        # note: using just 'e' is not always sufficient, e.g. for KeyErrors, it
        # just writes the key, not the helpful word "KeyError".
        # e.message would be helpful, but that's deprecated since Python 2.6.
        print("Problem {}: EXCEPTION. {}".format(problem_number, e))
