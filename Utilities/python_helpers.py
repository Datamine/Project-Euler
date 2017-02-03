#!/usr/bin/python3

from functools import reduce

def count_iterable(iterable):
    """
    useful for returning the length of a finite generator
    """
    return sum(1 for item in iterable)

def product(iterable):
    """
    computes the product of an iterable containing items on which multiplication
    is a valid operation, e.g. [1,2,3] or [Fraction(1,5), Fraction(2,3)], etc.
    """
    return reduce(lambda x,y: x*y, iterable)

def print_grid(nested_list):
    """
    for debugging
    """
    for row in nested_list:
        print(row)

def left_right_truncate(s):
    """
    iteratively removes characters from either end of the string, returns
    all substrings thus created.
    """
    resulting_strings = set([])

    for i in range(len(s)):
        resulting_strings.add(s[i:])
        resulting_strings.add(s[:i])

    resulting_strings.discard('')
    return resulting_strings

def are_permutations(*args):
    """
    tests whether string-arguments supplied are all permutations of one another
    """
    return
