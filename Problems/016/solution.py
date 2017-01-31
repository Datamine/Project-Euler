#!/usr/bin/python3

def main():
    # this is one of those problems where using Python just feels like cheating.
    return sum([int(c) for c in  str(2**1000)])

if __name__=='__main__':
	print(main())
