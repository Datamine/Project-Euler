#!/usr/bin/python3

def next_collatz(n):
    if n%2 == 0:
        return n // 2
    else:
        return (3 * n) + 1

def main():
    # store the number responsible for the longest chain
    record_number = 0
    max_chain_length = 0

    chain_lengths = {}

    for i in range(1, 1000000):
        n = i
        current_chain_length = 1
        while n != 1:
            if n in chain_lengths:
                # take advantage of memoized chain lengths to shortcut computations
                current_chain_length += chain_lengths[n]
                break
            n = next_collatz(n)
            current_chain_length += 1

        if n not in chain_lengths:
            chain_lengths[n] = current_chain_length

        if current_chain_length > max_chain_length:
            max_chain_length = current_chain_length
            record_number = i

    return record_number

if __name__=='__main__':
    print(main())
