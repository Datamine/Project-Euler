#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers

def main():
    sums_of_amicables = 0
    sums_of_divisors = {}
    for i in range(1,10000):
        # proper divisors only!
        s = sum([x for x in math_helpers.divisors(i) if x != i])
        if s <= 10000:
            # we're only considering values up to 10k
            sums_of_divisors[i] = s

    for key, value in sums_of_divisors.items():
        if key < value and sums_of_divisors.get(value) == key:
            # we can restrict to only looking where key < value because
            # the relationship is symmetrical -- this minimizes lookups
            sums_of_amicables += key + value

    return sums_of_amicables

if __name__=='__main__':
	print(main())
