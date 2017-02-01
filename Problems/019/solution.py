#!/usr/bin/python3

import datetime

def main():
    # this is a tedious problem and I am not going to implement the datetime algorithm.
    count = 0
    for year in range(1901, 2001):
        for month in range(1,13):
            date = datetime.date(year=year, month=month, day=1)
            if date.weekday() == 6:
                count +=1
    return count

if __name__=='__main__':
	print(main())
