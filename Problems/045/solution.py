#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers

def main():
    # key insight: all hexagonal numbers are triangular numbers. need to iterate
    # over hexagonal numbers and find a pentagonal > 40755.
    hex_numbers = math_helpers.hexagonal_number_generator()

    for h in hex_numbers:
        if h <= 40755:
            continue

        if math_helpers.is_pentagonal(h):
            return h

if __name__=='__main__':
    print(main())
