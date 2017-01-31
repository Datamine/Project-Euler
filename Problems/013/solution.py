#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def main():
    with open("Problems/013/numbers.txt","r") as f:
        return str(sum(map(lambda x: int(x.strip()), f.readlines())))[:10]

if __name__=='__main__':
    print(main())
