#!/usr/bin/python3
"""
tests for Utilities.primes
"""

import os, sys
sys.path.append(os.getcwd())

import unittest
from Utilities import primes

class PrimesUpTo(unittest.TestCase):
    """
    tests for Utilities.primes.primes_up_to
    """

    def test_case(self):
        """
        test that the primes_up_to function works as expected, including
        edge case arguments
        """

        with self.assertRaises(Exception):
            # have to call list() because these are lazily evaluated generators
            # error doesn't get thrown until you actually try to evaluate them
            list(primes.primes_up_to(-1))

        with self.assertRaises(Exception):
            list(primes.primes_up_to(0))

        with self.assertRaises(Exception):
            list(primes.primes_up_to(1))

        self.assertEqual(list(primes.primes_up_to(2)), [])
        self.assertEqual(list(primes.primes_up_to(5)), [2, 3])
        self.assertEqual(list(primes.primes_up_to(11)), [2, 3, 5, 7])
        self.assertEqual(list(primes.primes_up_to(12)), [2, 3, 5, 7, 11])

class PrimeNumbers(unittest.TestCase):
    """
    tests for Utilities.primes.prime_numbers
    """

    def test_case(self):
        """
        test that the prime_numbers generator works as expected.
        """

        generator = primes.prime_numbers()
        first_ten_primes = [next(generator) for x in range(10)]
        canonical_values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(first_ten_primes, canonical_values)

class PrimeFactors(unittest.TestCase):
    """
    tests for Utilities.primes.prime_factors
    """

    def test_case(self):
        """
        test that the prime factors are computed/outputted as expected.
        """

        self.assertEqual(primes.prime_factors(1), [])
        self.assertEqual(primes.prime_factors(2), [2])
        self.assertEqual(primes.prime_factors(8), [2, 2, 2])
        self.assertEqual(primes.prime_factors(20), [2, 2, 5])
        self.assertEqual(primes.prime_factors(67), [67])
        self.assertEqual(primes.prime_factors(120), [2, 2, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
