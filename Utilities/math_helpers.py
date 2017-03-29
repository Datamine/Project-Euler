#!/usr/bin/python3
from functools import reduce
from math import sqrt, ceil
from itertools import count, accumulate
from .python_helpers import count_iterable

def hexagonal_number_generator():
    """
    generator that yields the hexagonal numbers, starting from 1
    """
    natural_numbers = count(1)
    for n in natural_numbers:
        yield n * (2 * n - 1)

def pentagonal_number_generator():
    """
    generator that yields the pentagonal numbers, starting from 1
    """
    natural_numbers = count(1)
    for n in natural_numbers:
        yield (n * (3 * n - 1)) // 2

def is_pentagonal(n):
    """
    returns True if a number is a pentagonal number, False otherwise.
    """
    # inverse function of n(3n-1)/2. if result is an integer, then that natural number
    # yields that pentagonal number.
    res = (sqrt(24 * n + 1) + 1) / 6.0
    return res % 1 == 0

def triangle_number_generator(start=0):
    """
    generator that yields the triangle numbers
        - start: integer, dictates the starting natural number (use: index naturals from 0/1)
    """
    natural_numbers = count(start)
    triangle_number = 0
    for n in natural_numbers:
        triangle_number += n
        yield triangle_number

def first_n_triangle_numbers(n):
    """
    faster way to return the first n triangle numbers
    (starting at 1)
    """
    return accumulate(range(1,n+1))

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
