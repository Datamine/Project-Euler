#!/usr/bin/python3

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # in the following list, each index maps to the number of ways in which we can
    # make change for index pence. we pre-populate the trivial case: at index 0,
    # there is 1 way to make change for 0 pence.
    change_making_ways = [1] + [0] * 200
    for coin in coins:
        for amount in range(coin, 201):
            change_making_ways[amount] += change_making_ways[amount - coin]

    return change_making_ways[-1]

if __name__=='__main__':
    print(main())
