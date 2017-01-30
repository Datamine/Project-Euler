#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from functools import reduce

with open("008/long_number", "r") as f:
    long_number_string = ''.join(map(lambda x: x.strip(), f.readlines()))

max_product = 0

# string is 1000 digits long, we're interested in 13 adjacents. 
# so stop at 987. after that, < 13 adjacents.
for i in range(987):
    thirteen_ints = long_number_string[i:i+13]
    product = reduce(lambda a,b: a * b, [int(x) for x in thirteen_ints])
    if product > max_product:
        max_product = product

print max_product
