#!/usr/bin/python3

def fibonacci_numbers():
    """
    a generator of fibonacci numbers
    """
    first, second = 0, 1
    while True:
        new_element = first + second
        yield first
        first, second = second, new_element
