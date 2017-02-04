#!/usr/bin/python3
"""
tests for Utilities.math_helpers
"""

import os, sys
sys.path.append(os.getcwd())

import unittest
from Utilities import math_helpers

class HexagonalNumbers(unittest.TestCase):
    """
    tests for Utilities.math_helpers.hexagonal_number_generator
    """

    def test_generation(self):
        """
        test that the hexagonal number generator generates hexagonal numbers, as expected.
        """
        generator = math_helpers.hexagonal_number_generator()
        first_ten_hex_numbers = [next(generator) for _ in range(10)]
        canonical_values = [1, 6, 15, 28, 45, 66, 91, 120, 153, 190]
        self.assertEqual(canonical_values, first_ten_hex_numbers)

class PentagonalNumbers(unittest.TestCase):
    """
    tests for Utilities.math_helpers.pentagonal_number_generator
    """

    def test_generation(self):
        """
        test that the pentagonal number generator generates pentagonal numbers, as expected.
        """
        generator = math_helpers.pentagonal_number_generator()
        first_ten_pentagonal_numbers = [next(generator) for _ in range(10)]
        canonical_values = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
        self.assertEqual(canonical_values, first_ten_pentagonal_numbers)

class IsPentagonal(unittest.TestCase):
    """
    tests for Utilities.math_helpers.is_pentagonal
    """

    def test_first_thousand_pentagonal_numbers(self):
        """
        test that the first thousand pentagonal numbers are identified as such.
        """
        generator = math_helpers.pentagonal_number_generator()
        first_thousand_pentagonal_numbers = [next(generator) for _ in range(1000)]
        all_pentagonal = all(map(lambda x: math_helpers.is_pentagonal(x), first_thousand_pentagonal_numbers))
        self.assertEqual(all_pentagonal, True)

    def test_very_large_pentagonal_numbers(self):
        """
        test that even large pentagonal numbers are correctly identified as such
        (i.e. check whether we might expect to run into floating-point error)
        """
        large_n = [x**9 for x in range(10000,10500)]
        pentagonals = [(n * (3 * n - 1)) // 2 for n in large_n]
        all_pentagonal = all(map(lambda x: math_helpers.is_pentagonal(x), pentagonals))
        self.assertEqual(all_pentagonal, True)

    def test_not_pentagonal(self):
        """
        test some non-pentagonal numbers, make sure they don't show up as pentagonal.
        """
        generator = math_helpers.pentagonal_number_generator()
        pents = set(next(generator) for _ in range(1000))
        non_pentagonals = set(x for x in range(max(pents)) if x not in pents)
        any_pentagonals = any(map(lambda x: math_helpers.is_pentagonal(x), non_pentagonals))
        self.assertEqual(any_pentagonals, False)

class TriangleNumbers(unittest.TestCase):
    """
    tests for Utilities.math_helpers.triangle_number_generator
    """

    def test_generation_index_zero(self):
        """
        test that the generator yields the correct output when indexing from zero
        """
        generator = math_helpers.triangle_number_generator()
        first_eleven_triangle_numbers = [next(generator) for _ in range(11)]
        canonical_values = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(canonical_values, first_eleven_triangle_numbers)

    def test_generation_index_one(self):
        """
        test that the generator yields the correct output when indexing from one
        """
        generator = math_helpers.triangle_number_generator(1)
        first_ten_triangle_numbers = [next(generator) for _ in range(10)]
        canonical_values = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        self.assertEqual(canonical_values, first_ten_triangle_numbers)

class FirstNTriangleNumbers(unittest.TestCase):
    """
    tests for Utilities.math_helpers.first_n_triangle_numbers
    """

    def test_first_n_triangle_numbers(self):
        self.assertEqual(list(math_helpers.first_n_triangle_numbers(0)), [])
        self.assertEqual(list(math_helpers.first_n_triangle_numbers(1)), [1])
        self.assertEqual(list(math_helpers.first_n_triangle_numbers(5)), [1, 3, 6, 10, 15])

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
