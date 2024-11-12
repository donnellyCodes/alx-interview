#!/usr/bin/python3
"""
    Generates a Pascal's triangle of size n.
"""


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    # initialize triangle as an empty string
    triangle = []
    # checks if n is an integer and if n
    # is less than or equal to 0, returns an empty triangle
    if type(n) is not int or n <= 0:
        return triangle
    # outer loop iterates i and inner loop iterates j
    for i in range(n):
        line = []
        for j in range(i+1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(line)
    return triangle
