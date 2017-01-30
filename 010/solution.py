#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from Utilities import primes

primegen = primes.primes_up_to(2000000)
print(sum(primegen))
