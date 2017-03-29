#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers
from itertools import count

def main():
    natural_numbers = count(1)

    for n in natural_numbers:
        current_triangle_number = n * (n+1) //2
        # the nth triangular number is given by n * (n+1) * 1/2. Note that n and n+1
        # are necessarily coprime. If a, b coprime, then the number of divisors of a*b
        # is equal to the product of the numbers of divisors of a and b.
        if n%2==0:
            number_of_divisors = math_helpers.num_divisors(n//2) * math_helpers.num_divisors(n+1)
        else:
            number_of_divisors = math_helpers.num_divisors(n) * math_helpers.num_divisors((n+1)//2)

        if number_of_divisors > 500:
            return current_triangle_number

if __name__=='__main__':
    main()
