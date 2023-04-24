#!/usr/bin/python3
""" Pascals triangle """

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    # Print rows of the triangle in the desired format
    max_len = len(str(triangle[-1][len(triangle[-1]) // 2]))
    for row in triangle:
        row_str = ""
        for num in row:
            row_str += str(num).center(max_len)
        print(row_str)

