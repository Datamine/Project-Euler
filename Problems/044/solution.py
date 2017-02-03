#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers

def main():
    # minimizing D = |k -j| means to find the closest pair -- which
    # will be the first pair found. (Since the differences between
    # sequential pentagonal numbers are monotonically increasing in size.)

    pgen = math_helpers.pentagonal_number_generator()
    # generate the first 5000 pentagonal numbers.
    pentagonal_numbers = [next(pgen) for x in range(5000)]

    for k in pentagonal_numbers:
        for j in pentagonal_numbers:
            if math_helpers.is_pentagonal(abs(k-j)) and math_helpers.is_pentagonal(k+j):
                return abs(k-j)

if __name__=='__main__':
    print(main())
