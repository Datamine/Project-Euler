#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def alphabetical_value(string):
    """
    computes the alphabetical value of a name, where a = 1, z = 26, etc.
    """

    # ord('a') = 97, so subtract 96
    return sum(ord(x) - 96 for x in string)

def main():
    with open("Problems/022/p022_names.txt","r") as f:
        # names file is just one line
        names = sorted(map(lambda x: x.lower(), eval("[" + f.readline().strip() + "]")))

    sum_total = 0
    # start indexing from 1
    for index, name in enumerate(names, 1):
        sum_total += index * alphabetical_value(name)
    return sum_total

if __name__=='__main__':
	print(main())
