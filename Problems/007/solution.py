#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    gen = primes.prime_numbers(10001)

    for prime in gen:
        pass

    # exhaust the generator. this returns the final item.
    return prime

if __name__=='__main__':
    print(main())
