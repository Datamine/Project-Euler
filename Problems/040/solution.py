#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import python_helpers
from itertools import count, cycle

def main():
    # there also exists a pure paper-and-pencil way to solve this problem,
    # but it was faster for me to write up this solution

    product_list = []

    desired_digits = cycle([10**n for n in range(7)])
    currently_desired_digit = next(desired_digits)

    # line up count and digits_seen
    digits_seen = 0
    for n in count(1):
        # this is the inefficient way to proceed, but i'm ok with it -- it's still v fast
        for char in str(n):
            digits_seen += 1
            if digits_seen == currently_desired_digit:
                product_list.append(int(char))
                currently_desired_digit = next(desired_digits)
                if len(product_list) == 7:
                    return python_helpers.product(product_list)

if __name__=='__main__':
    print(main())
