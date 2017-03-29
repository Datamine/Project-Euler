#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import python_helpers
# use python_helpers.print_grid for debugging, if need be

def main():
    with open("Problems/018/triangle.txt", "r") as f:
        triangle = list(map(lambda x: list(map(int, x.strip().split(" "))), f.readlines()))

    # the correct approach is a dynamic/folding one: just add the
    # maximum adjacent number, so as to keep cumulative running totals

    for row_index, row in enumerate(triangle):
        if row_index == 0:
            continue

        for col_index, _ in enumerate(row):
            # the two adjacent numbers are, relative to the current number,
            # at the same col_index, and at col_index - 1 (unless col_index = 0,
            # or col_index is the last in that row, in which case the current
            # number has only one adjacent number).
            adjacent_numbers = []
            if col_index != 0:
                adjacent_numbers.append(triangle[row_index - 1][col_index - 1])
            if col_index != len(row)-1:
                adjacent_numbers.append(triangle[row_index - 1][col_index])
            triangle[row_index][col_index] += max(adjacent_numbers)

    # return max element in last row
    return max(triangle[-1])

if __name__=='__main__':
	print(main())
