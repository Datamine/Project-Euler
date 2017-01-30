#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import fibonacci

# Note that Project Euler starts the Fibonacci Sequence with 1, 2, 3, ...
# whereas I start mine with 0, 1, 1, ... the difference doesn't matter because 1 is odd.

even_fibonacci_numbers = filter(lambda x: x%2==0, fibonacci.fibonacci_numbers(4000000))
print(sum(even_fibonacci_numbers))
