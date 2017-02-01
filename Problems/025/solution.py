#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import fibonacci

def main():
    fibgen = fibonacci.fibonacci_numbers()
    # the problem asks to index from 1, but the problem also starts the Fib
    # sequence with 1, 1, 2, 3, ... whereas I start my generator with 0, 1, 1, 2, ...
    # so it's okay to index from 0 here.
    for index, f in enumerate(fibgen):
        if len(str(f)) >= 1000:
            return index

if __name__=='__main__':
	print(main())
