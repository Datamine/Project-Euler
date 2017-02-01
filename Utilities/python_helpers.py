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

def print_grid(nested_list):
    """
    for debugging
    """
    for row in nested_list:
        print(row)

def left_and_right_truncate(s):
    resulting_strings = set([])

    for i in range(len(s)):
        resulting_strings.add(s[i:])
        resulting_strings.add(s[:i])

    resulting_strings.discard('')
    return resulting_strings
