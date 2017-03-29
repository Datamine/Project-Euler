#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    gen = primes.prime_numbers()

    for index, prime in enumerate(gen):
        if index == 10000:
            return prime

if __name__=='__main__':
    print(main())
