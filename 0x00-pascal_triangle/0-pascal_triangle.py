#!/usr/bin/python3
""" Pascals triangle ALX Interview """


def pascal_triangle(n):
    """Returns a pascal's triangle as per specs in README"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        """ Output variations """
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for m in range(1, i):
            """ Fit values into the output format"""
            if m > 0 and m < len(row):
                x = pascal_triangle[i - 1][m]
                y = pascal_triangle[i - 1][m - 1]
                row[m] = x + y

        pascal_triangle[i] = row

    return pascal_triangle
