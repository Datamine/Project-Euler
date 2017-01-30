#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import math

current_natural_number = 1

while True:
    current_natural_number += 1
    current_triangle_number = current_triangle_number * (current_triangle_number + 1) / 2    

    if num_divisors(current_triangle_number) > 500:
        print current_triangle_number
        break
