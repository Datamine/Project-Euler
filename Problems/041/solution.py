#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    largest_pandigital_prime = 0

    # the largest possible n is 9, since we have 9 digits available.
    # at first this looks as if we've got a very large search space. but fear not!
    # a number is divisible by 3 (i.e. not prime) if the sum of its digits is divisible by 3.
    # it turns out that sum(range(10)) = 45, which is divisible by 3. So no 9-digit
    # pandigital numbers are primes. sum(range(9)) = 36, also divisible by 3.
    # So no 8-digit pandigital numbers are primes.
    # Sum(range(8)) = 28, so there may be 7-digit pandigital primes.
    # Sum(range(7)) = 21, so there are no 6-digit pandigital primes.
    # Sum(range(6)) = 15, so there are no 5-digit pandigital primes.
    # Sum(range(5)) = 10, so there may be 4-digit pandigital primes.
    # We already know from the problem that 2143 is one.

    # We consider all the primes up to the maximum 7-digit pandigital.
    prime_numbers = primes.primes_up_to(7654321 + 1)

    for p in prime_numbers:
        if p > 4321 and p < 1234567:
            # skip the impossible values
            continue

        strp = str(p)
        l = len(strp)
        # pandigital check: no duplicates, max element is same as length
        if l == len(set(strp)) and int(max(strp)) == l and p > largest_pandigital_prime:
            largest_pandigital_prime = p

    return largest_pandigital_prime

if __name__=='__main__':
    print(main())
