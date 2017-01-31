#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers

triangle_numbers = math_helpers.triangle_numbers()

for n in triangle_numbers:
    # the nth triangular number is given by n * (n+1) * 1/2. Note that n and n+1
    # are necessarily coprime. If a, b coprime, then the number of divisors of a*b
    # is equal to the product of the numbers of divisors of a and b.
    if n%2==0:
        number_of_divisors = math_helpers.num_divisors(n//2) * math_helpers.num_divisors(n+1)
    else:
        number_of_divisors = math_helpers.num_divisors(n) * math_helpers.num_divisors((n+1)//2)

    print(n, number_of_divisors)
    if number_of_divisors > 20:
        print(n)
        break
