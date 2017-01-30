#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

gen = primes.prime_numbers(10001)

for prime in gen:
    pass

print(prime)
