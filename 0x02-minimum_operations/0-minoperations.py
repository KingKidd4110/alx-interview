#!/usr/bin/python3
""" minimum operations """


def minOperations(n):
    """
    Number of minimum operations that can be performed
    """
    i = 0
    min_i = 2
    while n > 1:
        while n % min_i == 0:
            i += min_i
            n /= min_i
        min_i += 1
    return i
