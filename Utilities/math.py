#!/usr/bin/python3
from functools import reduce
from math import sqrt

def product(l):
    """
    computes the product of an iterable
    """
    return reduce(lambda x,y: x*y, l)

def divisors(n):
    """
    returns the list of divisors of a number
    """
    divs = []
    for i in range(sqrt(n)):
        if n % i == 0:
            
