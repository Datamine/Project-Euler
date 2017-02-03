#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    # I'll try doing this with values up to a million -- I assume the solution
    # is smaller than that.

    # store these separately as lists and sets for faster lookup (set) and iteration (list)
    twice_squares_list = [2 * x**2 for x in range(1000) if 2 * x**2 <= 1000000]
    twice_squares_set = set(twice_squares_list)
    prime_numbers = set(primes.primes_up_to(1000000))

    # step 2 since odd numbers only
    for i in range(3,1000000,2):
        if not i in prime_numbers:
            for s in twice_squares_list:
                if s >= i:
                    return i
                difference = i - s
                if difference in prime_numbers:
                    break


if __name__=='__main__':
    print(main())
