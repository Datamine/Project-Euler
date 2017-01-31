#!/usr/bin/python3

def printgrid(grid):
    """
    for debugging
    """
    for row in grid:
        print(row)

def main():
    # dynamic programming problem. The trick is to realize that the number of paths
    # to a given square is the sum of the number of paths to square to the left
    # and to the right. then proceed iteratively and fill out the grid.
    grid_size = 20
    grid = [[None] * 20 for i in range(20)]

    for row_index, row in enumerate(grid):
        for col_index, _ in enumerate(row):
            if row_index == 0:
                paths_above = 1
            else:
                paths_above = grid[row_index - 1][col_index]

            if col_index == 0:
                paths_left = 1
            else:
                paths_left = grid[row_index][col_index - 1]

            grid[row_index][col_index] = paths_left + paths_above

    # it's noteworthy that the sum-left/sum-above stuff is basically the binomial
    # expansion. To solve this problem, you can also just compute the middle coefficient
    # for the 20th binomial expansion. I suggest you look at the 4x4 case to see this.
    return grid[-1][-1]

if __name__=='__main__':
	print(main())
