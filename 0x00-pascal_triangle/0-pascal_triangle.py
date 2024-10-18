#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates a Pascal's triangle of size n.
    """
    # if n is less than or equal to 0, return empty list
    if n <= 0:
        return []
    
    # initialize first row with 1
    triangle = [[1]]
    
    
    # loop to generate each row of the triangle
    for i in range(1, n):
        # start each row with 1
        row = [1]
        
        # loop to calculate each element in the row except the first and last
        for j in range(1, i):
            # each value is the sum of the two values directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # append the last element of the current row to the triangle
        row.append(1)
        
        # append the current row to the triangle
        triangle.append(row)
    # return the completed Pascal's triangle
    return triangle