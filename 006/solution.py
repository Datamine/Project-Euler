#!/usr/bin/python3

sum_of_squares_accumulator = 0

for i in range(1,101):
    sum_of_squares_accumulator += i**2

square_of_sum = sum(range(1,101)) ** 2

# print the difference
print(abs(square_of_sum - sum_of_squares_accumulator))
