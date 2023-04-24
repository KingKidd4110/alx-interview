#!/usr/bin/python3
""" Pascals triangle """


def pascal_triangle(n):
    """ Prints Pascals triangle using specs on README """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        """ Define output variables """
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    """ Print rows of the triangle in the desired format """
    for row in triangle:
        print(row)
