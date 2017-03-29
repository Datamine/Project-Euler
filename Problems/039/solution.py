#!/usr/bin/python3

from math import ceil

def main():
    number_of_solutions = dict((x,0) for x in range(1000))

    # p must always be even. you can prove this by taking a+b+c=p and a^2+b^2=c^2
    # and plugging in odd/even values of a and b.
    for p in range(2, 1000, 2):
        # the maximum potential c is half the total perimeter. see triangle inequality: a + b >= c.
        potential_c_values = range(1, int(ceil(p/2)))
        for c in potential_c_values:
            remainder = p - c
            potential_ab_values = range(1, remainder)
            for b in potential_ab_values:
                a = remainder - b
                if a <= b and a**2 + b**2 == c**2:
                    # a <= b, else we double-count combinations like (3, 4, 5) and (4, 3, 5)
                    number_of_solutions[p] += 1

    return max(number_of_solutions, key=lambda k: number_of_solutions[k])

if __name__=='__main__':
    print(main())
