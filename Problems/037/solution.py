#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes
from Utilities import python_helpers

def main():
    primegen = primes.prime_numbers()
    # cheating a little: I didn't know how these primes are distributed, so on my first attempt,
    # I generated the first million primes. That took a while. The result showed I actually
    # only neeeded to generate far fewer primes.
    cached_primes = set(next(primegen) for x in range(75000))
    result_primes = []

    for prime in cached_primes:
        truncated = map(int, python_helpers.left_right_truncate(str(prime)))
        if all(t in cached_primes for t in truncated):
            if prime in [2,3,5,7]:
                # remember that the problem statement asked us to exclude 2,3,5,7.
                continue
            result_primes.append(prime)
            if len(result_primes) == 11:
                return sum(result_primes)

if __name__=='__main__':
    print(main())
