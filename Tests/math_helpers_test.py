#!/usr/bin/python3
"""
tests for Utilities.math_helpers
"""

import os, sys
sys.path.append(os.getcwd())

import unittest
from Utilities import math_helpers

class TriangleNumbers(unittest.TestCase):
    """
    tests for Utilities.math_helpers.triangle_numbers()
    """

    def test_generation(self):
        """
        test that the generator yields the correct output
        """
        generator = math_helpers.triangle_numbers()
        first_ten_triangle_numbers = [next(generator) for _ in range(11)]
        canonical_values = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(canonical_values, first_ten_triangle_numbers)

class Divisors(unittest.TestCase):
    """
    tests for Utilities.math_helpers.divisors(n)
    """

    def test_error_case(self):
        """
        divisors(n) should throw errors if given input that is n < 1 or not a whole number.
        """
        with self.assertRaises(ValueError):
            list(math_helpers.divisors(0))

        with self.assertRaises(ValueError):
            list(math_helpers.divisors(-2))

        with self.assertRaises(ValueError):
            list(math_helpers.divisors(3.5))

    def test_small_cases(self):
        """
        test that it returns the correct output for small values
        """
        case_one = list(math_helpers.divisors(1))
        self.assertEqual(case_one, [1])

        case_two = math_helpers.divisors(2)
        self.assertCountEqual(case_two, [1, 2])

        case_three = math_helpers.divisors(10)
        self.assertCountEqual(case_three, [1, 2, 5, 10])

        case_four = math_helpers.divisors(21)
        self.assertCountEqual(case_four, [1, 21, 3, 7])

        case_five = math_helpers.divisors(37)
        self.assertCountEqual(case_five, [1, 37])

        case_six = math_helpers.divisors(128)
        self.assertCountEqual(case_six, [1, 2, 4, 8, 16, 32, 64, 128])

        case_seven = math_helpers.divisors(11029)
        self.assertCountEqual(case_seven, [1, 41, 269, 11029])

        case_eight = math_helpers.divisors(6930)
        self.assertCountEqual(case_eight, [1, 2, 3, 5, 6, 7, 9, 10, 11, 14, 15, 18, 21, 22,
                                           30, 33, 35, 42, 45, 55, 63, 66, 70, 77, 90, 99,
                                           105, 110, 126, 154, 165, 198, 210, 231, 315, 330,
                                           385, 462, 495, 630, 693, 770, 990, 1155, 1386,
                                           2310, 3465, 6930])

class NumDivisors(unittest.TestCase):
    """
    tests for Utilities.math_helpers.divisors(n)
    """

    def test_cases(self):
        """
        test that we get the correct output
        """
        case_one = math_helpers.num_divisors(1)
        self.assertEqual(case_one, 1)

        case_two = math_helpers.num_divisors(10)
        self.assertEqual(case_two, 4)

        case_three = math_helpers.num_divisors(6930)
        self.assertEqual(case_three, 48)



if __name__ == '__main__':
    unittest.main()
