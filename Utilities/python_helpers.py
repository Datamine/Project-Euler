#!/usr/bin/python3

from functools import reduce

def count_iterable(iterable):
    """
    useful for returning the length of a finite generator
    """
    return sum(1 for item in iterable)

def product(iterable):
    """
    computes the product of an iterable containing numbers e.g. [1,2,3]
    """
    return reduce(lambda x,y: x*y, iterable)
