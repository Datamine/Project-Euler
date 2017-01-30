#!/usr/bin/python3

number = 600851475143
largest_factor = 1

current_divisor = 1
while (current_divisor**2 < number):
    if number % current_divisor == 0:
        number = number / current_divisor
        largest_factor = current_divisor
    
    current_divisor += 1

# if a * b = n, then print the larger of a, b
if number > largest_factor:
    largest_factor = number

print(largest_factor)
