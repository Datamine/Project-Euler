#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

def main():
    with open('Problems/011/grid','r') as f:
        # reads in the grid and transforms into a matrix of integers
        grid = list(map(lambda x: list(map(int, x.strip().split(' '))), f.readlines()))

    max_product = 0

    # horizontal and vertical case
    for i in range(20):
        for j in range(16):
            horizontal_prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            vertical_prod = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
            m = max(horizontal_prod, vertical_prod)
            if m > max_product:
                max_product = m

    # diagonal case: down/right
    for i in range(16):
        for j in range(16):
            p = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if p > max_product:
                max_product = p

    # diagonal case: down/left
    for i in range(3,20):
        for j in range(16):
            p = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if p > max_product:
                max_product = p

    return max_product

if __name__=='__main__':
    print(main())
