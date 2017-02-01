#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    # caching the first thousand primes. it seems unlikely that we'll need more.
    primegen = primes.prime_numbers()
    first_thousand_primes = set([next(primegen) for x in range(1000)])
    max_number_of_primes = 0
    corresponding_coefficients_product = 0

    for a in range(-1000,1000):
        for b in range(-1000,1000):
            n = 0
            while (n**2 + (a*n) + b) in first_thousand_primes:
                n+=1
            if n > max_number_of_primes:
                max_number_of_primes = n
                corresponding_coefficients_product = a * b

    return corresponding_coefficients_product

if __name__=='__main__':
    print(main())
