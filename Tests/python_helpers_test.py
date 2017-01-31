#!/usr/bin/python3
"""
tests for Utilities.python_helpers
"""

import os, sys
sys.path.append(os.getcwd())

import unittest
from Utilities import python_helpers

class Product(unittest.TestCase):
    """
    tests for Utilities.python_helpers.product
    """

    def test_case(self):
        """
        test that product returns the correct output
        """
        case_one = python_helpers.product([1])
        self.assertEqual(case_one, 1)

        case_two = python_helpers.product([1, 2])
        self.assertEqual(case_two, 2)

        case_three = python_helpers.product([1, 2, 5, 10])
        self.assertEqual(case_three, 100)

class CountIterable(unittest.TestCase):
    """
    tests for Utilities.python_helpers.count_iterable
    """

    def test_case(self):
        """
        test that count_iterable returns the correct counts
        """
        case_zero = python_helpers.count_iterable([])
        self.assertEqual(case_zero, 0)

        case_one = python_helpers.count_iterable(range(10))
        self.assertEqual(case_one, 10)

        case_two = python_helpers.count_iterable([1,2,3])
        self.assertEqual(case_two, 3)

if __name__ == '__main__':
    unittest.main()
