#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def main():
    longest_cycle = 0
    longest_cycle_denominator = 0

    for denominator in range(2, 1001):
        for x in range(1, denominator):
            if 10**x % denominator == 1:
                cycle_length = x
                break
        else:
            cycle_length = 0
        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            longest_cycle_denominator = denominator

    # incidentally, the longest cycle is 982, and the denominator is 983. I wonder what's going on there...
    return longest_cycle_denominator

if __name__=='__main__':
	print(main())
