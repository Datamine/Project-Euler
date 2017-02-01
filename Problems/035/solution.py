#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes
from collections import deque

def main():
    prime_numbers = set(map(str, primes.primes_up_to(1000000)))
    count = 0

    for p in prime_numbers:
        deque_prime = deque(p)
        deque_prime.rotate(1)
        rotated_prime = ''.join(deque_prime)
        while rotated_prime in prime_numbers:
            if rotated_prime == p:
                # when we've cycled over the prime successfully once
                count +=1
                break
            deque_prime.rotate(1)
            rotated_prime = ''.join(deque_prime)

    return count

if __name__=='__main__':
    print(main())
