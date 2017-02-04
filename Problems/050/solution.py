#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

def main():

    prime_number_list = list(primes.primes_up_to(1000000))
    # for faster lookups
    prime_number_set = set(prime_number_list)

    max_sequence_length = 0
    corresponding_prime = 0

    for index, prime in enumerate(prime_number_list):
        sequence_length = 0
        total = 0
        for sub_prime in prime_number_list[index:]:
            total += sub_prime
            if total > 1000000:
                break

            sequence_length += 1
            if total in prime_number_set and sequence_length > max_sequence_length:
                max_sequence_length = sequence_length
                corresponding_prime = total

    return corresponding_prime

if __name__=='__main__':
    print(main())
