#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers
from itertools import product

def main():
    abundant_numbers = []
    # find all the relevant abundant numbers
    for i in range(1, 28124):
        # proper divisors only
        s = sum(x for x in math_helpers.divisors(i) if x != i)
        if s > i:
            abundant_numbers.append(i)

    sums_of_pairs = set([])
    for a in abundant_numbers:
        for b in abundant_numbers:
            if b > a:
                break
            x = a + b
            if x < 28124:
                sums_of_pairs.add(x)

    ints = set(range(1,28124))

    return sum(ints - sums_of_pairs)

if __name__=='__main__':
    print(main())
