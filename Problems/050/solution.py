#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes
from itertools import accumulate

def main():

    prime_numbers = primes.primes_up_to(1000000)
    prime_sums_cumulative = list(accumulate(prime_numbers))
    # for faster lookups
    prime_number_set = set(prime_numbers)

    max_consecutives = 0
    corresponding_prime = 0

    for s1 in prime_sums_cumulative:
        for s2 in prime_sums_cumulative:
            if s1 - s2 > 1000000:
                break
            if s1 - s2 in prime_number_set:
                print(s1-s2)
                number_consecutives = prime_sums_cumulative.index(s1) - prime_sums_cumulative.index(s2)
                if number_consecutives > max_consecutives:
                    max_consecutives = number_consecutives
                    corresponding_prime = prime_numbers[prime_sums_cumulative.index(s1)]
    return corresponding_prime

if __name__=='__main__':
    print(main())
