#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():
    primegen = primes.primes_up_to(2000000)
    return sum(primegen)

if __name__=='__main__':
    print(main())
