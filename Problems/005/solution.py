#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes
from collections import Counter
from functools import reduce

# use prime factorization. We want the product of the set of largest numbers
# that factor to all the integers between 1 and 20.
# I've used a programmatic approach here so that this can easily be adapted
# for larger ranges, if need be.

def main():
    relevant_integers = range(1,21)
    prime_factor_lists = [primes.prime_factors(n) for n in relevant_integers]

    # combined_factors: { prime factor : number of occurrences }, e.g. 8 would have {2: 3}
    combined_factors = {}
    for pf in prime_factor_lists:
        pf_count = Counter(pf)
        for key, value in pf_count.items():
            # check if the combined_factors already include this prime factorization
            # e.g. the prime factorization of 20 (2,2,5) includes that of 4 (2,2).
            if key in combined_factors:
                if combined_factors[key] < value:
                    combined_factors[key] = value
            else:
                combined_factors[key] = value

    product = 1
    for key, value in combined_factors.items():
        product *= (key ** value)

    return product

if __name__=='__main__':
    print(main())
