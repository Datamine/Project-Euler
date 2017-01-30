#!/usr/bin/python3

def fibonacci_numbers(n):
    """
    a generator of fibonacci numbers up to the element exceeding n.
    """
    first, second = 0, 1
    while True:
        new_element = first + second
        yield first
        if new_element < n:
            first, second = second, new_element
        else:
            yield second
            return


