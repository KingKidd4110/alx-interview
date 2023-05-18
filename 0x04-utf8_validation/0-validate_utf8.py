#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Declare number of bytes"""
    num_bytes = 0

    for byte in data:
        if (byte & 0b11000000) == 0b10000000:
            if num_bytes == 0:
                return False

            num_bytes -= 1
        else:
            if num_bytes > 0:
                return False

            if (byte & 0b10000000) == 0:
                num_bytes = 0
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False

    if num_bytes > 0:
        return False

    return True
