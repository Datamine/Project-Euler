#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math_helpers

def main():
    number_of_triangle_words = 0

    with open("Problems/042/p042_words.txt","r") as f:
        # words is a one-line file
        words = map(lambda x: x.lower(), eval("[" + f.readline().strip() + "]"))

    # assuming we won't need more than the first 100 triangle numbers, these words
    # should be short. set for fast membership tests.
    triangle_numbers = set(math_helpers.first_n_triangle_numbers(100))

    for word in words:
        # ord('a') = 97, so subtract 96 to get to the alphabetical enumeration
        word_sum = sum([ord(char) - 96 for char in word])
        if word_sum in triangle_numbers:
            number_of_triangle_words += 1

    return number_of_triangle_words

if __name__=='__main__':
    print(main())
