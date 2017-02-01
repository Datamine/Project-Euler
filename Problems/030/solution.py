#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def main():
    # note that 9^5 = 59,049. So the maximum sum of digits to the fifth power,
    # for a four-digit number, for example, is 4 * 9^5 = 236,196. For a seven-digit
    # number, however, 7 * 9^5 = 413,343, which is smaller than the smallest seven-digit number.
    # so this suggests we only need to check through the six-digit-numbers, where
    # the largest possible such number is 6 * 9^5 = 354,294.

    accumulator = 0
    # start the range at 10. according to the problem, single-digit numbers do not create sums,
    # which i disagree with, but so be it.
    for i in range(10, 354295):
        fifth_digit_sum = sum(int(c)**5 for c in str(i))
        if fifth_digit_sum == i:
            accumulator += i

    return accumulator

if __name__=='__main__':
    print(main())
