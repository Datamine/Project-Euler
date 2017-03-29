#!/usr/bin/python3

from fractions import gcd

# use euclid's formula to generate pythagorean triples
# https://en.wikipedia.org/wiki/Pythagorean_triple

def main():
    # c = m^2 + n ^2 so the largest possible m is 32, m > n > 0
    for m in range(33):
        for n in range(m):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if a + b + c == 1000:
                return a * b * c

if __name__=='__main__':
    print(main())
