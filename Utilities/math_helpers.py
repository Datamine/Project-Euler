#!/usr/bin/python3
from functools import reduce
from math import sqrt, ceil
from .python_helpers import count_iterable

def triangle_numbers():
    """
    generator that yields a list of triangle numbers
    """
    triangle_number = 0
    natural_number = 0
    while True:
        triangle_number += natural_number
        yield triangle_number
        natural_number +=1

def divisors(n):
    """
    generator that yields the divisors of n, unsorted
    """
    if n < 1 or (not n%1==0):
        raise ValueError("Input to divisors must be an integer greater than or equal to one.")

    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i**2 != n:
                yield n//i

def num_divisors(n):
    """
    returns the number of divisors of n.
    """
    divs = divisors(n)
    return count_iterable(divs)
