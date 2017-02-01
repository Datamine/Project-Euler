#!/usr/bin/python3

def primes_up_to(max_prime):
    """
    generates prime numbers smaller than max_prime.
    adapted from: http://stackoverflow.com/a/3941967
    """
    prime_flags = [True] * max_prime
    prime_flags[0] = prime_flags[1] = False
    for index, flag in enumerate(prime_flags):
        if flag:
            yield index
            for n in range(index**2, max_prime, index):
                prime_flags[n] = False

def prime_numbers():
    """
    generates indefinitely many prime numbers.
    """
    n = 2
    primes = []
    while True:
        is_prime = True
        for p in primes:
            if p**2 > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 1

def prime_factors(n):
    """
    returns the list of prime factors of n.
    """
    factors = []
    current_factor = 2

    while n > 1:
        while n % current_factor == 0:
            factors.append(current_factor)
            n /= current_factor
        current_factor += 1
        if current_factor ** 2 > n:
            if n > 1:
                factors.append(n)
            break

    # choosing not to return the map object, may change if needed
    return list(map(int, factors))
