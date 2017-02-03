#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def are_permutations(*args):
    # this is a bit of a gross implementation, but it works and it's fast
    arg_strings = list(map(str, args))
    first_l = len(set(arg_strings[0]))
    return all(len(set(x)) == first_l for x in arg_strings) and len(set(''.join(arg_strings))) == first_l

def main():
    # set and list for faster iteration & lookup, respectively
    prime_numbers = [x for x in primes.primes_up_to(9999) if x > 1000]
    primes_set = set(prime_numbers)

    # three primes, c > a > b, where c = a + k = b + 2k
    for a in prime_numbers:
        for b in prime_numbers:
            if b >= a:
                break
            c = a + (a - b)

            if c in primes_set and are_permutations(a,b,c) and (not a in [1487, 4817, 8147]):
                return ''.join([str(b), str(a), str(c)])

if __name__=='__main__':
    print(main())
