#!/usr/bin/python3
"""
tests for Utilities.fibonacci
"""

import os, sys
sys.path.append(os.getcwd())

import unittest
from Utilities import fibonacci

class FibonacciNumbers(unittest.TestCase):
    """
    tests for Utilities.fibonacci.fibonacci_numbers
    """

    def test_generation(self):
        """
        test that the fibonacci number generator generates fibonacci numbers, as expected
        """
        gen = fibonacci.fibonacci_numbers()
        first_ten_fib_numbers = [next(gen) for _ in range(10)]
        canonical_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(canonical_values, first_ten_fib_numbers)

if __name__ == '__main__':
    unittest.main()
