#!/usr/bin/python3
'''
Function that returns island perimeter decribed using grid
'''


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the given grid.
    Args:
    grid (list of list of int):
        grid where 0 represents water and 1 represents land.
    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # start with 4 sides of the square
                perimeter += 4

                # check the cell above
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # check the cell to the left
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # subtract 2 from shared sides
    return perimeter
