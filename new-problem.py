#!/usr/bin/python3

import os, sys
new_problem = sys.argv[1]
current_path = os.getcwd()

if not os.path.exists(new_problem):
    os.mkdir(new_problem)

filetext = ["#!/usr/bin/python3\n", "\n", "import os, sys\n", "sys.path.append(os.getcwd())\n"]
filepath = os.path.join(current_path, new_problem, "solution.py")

with open(filepath, "w") as f:
    f.writelines(filetext)
