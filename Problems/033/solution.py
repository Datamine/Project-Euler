#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import python_helpers
import fractions

def main():
    # this solution is a little bit verbose in the number of variables and
    # conditionals, but I've tried to be clear about how I arrive at the solution,
    # rather than to write a terse statement that's much harder to parse.

    target_fractions = []

    # structure the loops to ensure numerator/denominator < 1
    for denominator in range(10,100):
        for numerator in range(10,denominator):
            if numerator%10 == 0 or numerator == denominator:
                # skip trivial cases
                continue

            str_d = str(denominator)
            str_n = str(numerator)
            intersection = [x for x in str_d if x in str_n]
            for common_element in intersection:
                # note that the only possibilities are for there to be zero or one common elements
                new_numerator = str_n.replace(common_element, '')
                new_denominator = str_d.replace(common_element, '')
                if len(new_numerator) == 1 and len(new_denominator) == 1 and new_denominator != '0' and new_numerator != '0':
                    incorrectly_reduced_fraction = fractions.Fraction(int(new_numerator), int(new_denominator))
                    correctly_reduced_fraction = fractions.Fraction(numerator, denominator)
                    if incorrectly_reduced_fraction == correctly_reduced_fraction:
                        target_fractions.append(correctly_reduced_fraction)

    return python_helpers.product(target_fractions)._denominator

if __name__=='__main__':
    print(main())
