#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from itertools import permutations

def main():
    # itertools.permutations even yields its result in lex-sorted order...
    p = permutations(range(10))
    for index, perm in enumerate(p):
        if index == 999999:
            return ''.join(map(str, list(perm)))

if __name__=='__main__':
	print(main())
