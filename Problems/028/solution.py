#!/usr/bin/python3

def main():
    # think of the spiral as a set of nested squares, where the side length grows
    # o-n every level by two (one integer on each side). then we try to capture all
    # the corner points on that level.

    # skipping the special case of the square of length one -- including that in the acc
    accumulator = 1
    # keep track of the number of values contained in previous squares/the maximum natural number up to now
    number_of_values_covered = 1
    for side_length in range(3,1002,2):
        corner_one = number_of_values_covered + side_length - 1
        corner_two = number_of_values_covered + 2 * (side_length - 1)
        corner_three = number_of_values_covered + 3 * (side_length - 1)
        corner_four = number_of_values_covered + 4 * (side_length - 1)
        number_of_values_covered = corner_four
        accumulator += corner_one + corner_two + corner_three + corner_four

    return accumulator

if __name__=='__main__':
    print(main())
