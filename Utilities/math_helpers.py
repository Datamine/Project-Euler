#!/usr/bin/python3
from functools import reduce
from math import sqrt, ceil
from itertools import count
from .python_helpers import count_iterable

def triangle_number_generator(start=0):
    """
    generator that yields a the triangle numbers
        - start: integer, dictates the starting natural number (use: index naturals from 0/1)
    """
    natural_numbers = count(start)
    triangle_number = 0
    for n in natural_numbers:
        triangle_number += n
        yield triangle_number

def divisors(n):
    """
    generator that yields the divisors of n, unsorted
        - n: integer
    """
    if n < 1 or (not n%1==0):
        raise ValueError("Input to divisors must be an integer greater than or equal to one. Offender: {}".format(n))

    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i**2 != n:
                yield n//i

def num_divisors(n):
    """
    returns the number of divisors of n.
        - n: integer
    """
    divs = divisors(n)
    return count_iterable(divs)
