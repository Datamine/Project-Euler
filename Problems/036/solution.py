#!/usr/bin/python3

def main():
    accumulator = 0
    for i in range(1000000):
        base_ten = str(i)
        binary = bin(i)[2:]
        if base_ten == base_ten[::-1] and binary == binary[::-1]:
            accumulator += i
    return accumulator

if __name__=='__main__':
    print(main())
