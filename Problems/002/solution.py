#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import fibonacci

# Note that Project Euler starts the Fibonacci Sequence with 1, 2, 3, ...
# whereas I start mine with 0, 1, 1, ... the difference doesn't matter because 1 is odd.

def main():
    sum_even_fibonacci_numbers = 0
    for f in fibonacci.fibonacci_numbers():
        if f > 4000000:
            break
        if f % 2 == 0:
            sum_even_fibonacci_numbers += f
    return sum_even_fibonacci_numbers

if __name__=='__main__':
    print(main())
