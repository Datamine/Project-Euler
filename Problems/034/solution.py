#!/usr/bin/python3

from math import factorial

def main():
    # first we need to find the upper bound, up to which we should check numbers.
    # note that 9! = 362,880, the maximum for any digit. Thus, 7 * 9! = 2,540,160,
    # but 8 * 9! = 2,903,040 -- and any 8-digit number is larger. Consequently,
    # we need to check exactly up to and including 2,540,160.

    accumulator = 0

    # problem statement asks to exclude 1, 2
    for i in range(3, 2540160):
        s = sum(factorial(int(x)) for x in str(i))
        if s == i:
            accumulator += i

    return accumulator

if __name__=='__main__':
    print(main())
