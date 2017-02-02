#!/usr/bin/python3

from itertools import permutations

def main():
    # it's interesting to me that in all these pandigital problems, I've approached
    # pandigital numbers in a different way every time. NB it's also possible to solve
    # this one using purely paper-and-pen.

    pandigital_numbers = permutations('1234567890')
    total = 0

    for p in pandigital_numbers:
        if p[0] == '0':
            # numbers with leading zeroes are not admissible
            continue

        p = ''.join(p)
        if (int(p[1:4])%2 == 0 and
                int(p[2:5])%3 == 0 and
                int(p[3:6])%5 == 0 and
                int(p[4:7])%7 == 0 and
                int(p[5:8])%11 == 0 and
                int(p[6:9])%13 == 0 and
                int(p[7:])%17 == 0):
            total += int(p)

    return total

if __name__=='__main__':
    print(main())
