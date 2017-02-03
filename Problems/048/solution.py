#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def main():
    # This is yet another problem where using a modern programming language like
    # Python as opposed to C makes the problem trivial...

    # fun fact: 0**0 == 1, hence we start the range at 1
    return str(sum(x**x for x in range(1,1001)))[-10:]

if __name__=='__main__':
    print(main())
