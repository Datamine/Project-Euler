#!/usr/bin/python3

from math import factorial

def main():
    return sum(int(i) for i in str(factorial(100)))

if __name__=='__main__':
	print(main())
