#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from itertools import count
from Utilities import primes

def main():

    for n in count(1):
        if (len(set(primes.prime_factors(n))) == 4 and
                len(set(primes.prime_factors(n+1))) == 4 and
                len(set(primes.prime_factors(n+2))) == 4 and
                len(set(primes.prime_factors(n+3))) == 4):
            return n

if __name__=='__main__':
    print(main())
