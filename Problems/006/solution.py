#!/usr/bin/python3

def main():
    sum_of_squares_accumulator = 0

    for i in range(1,101):
        sum_of_squares_accumulator += i**2

    square_of_sum = sum(range(1,101)) ** 2

    return abs(square_of_sum - sum_of_squares_accumulator)

if __name__=='__main__':
    print(main())
