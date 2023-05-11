#!/usr/bin/python3
"""
interview script
"""
import sys


total_file_size = 0

status_code_counts = {200: 0, 301: 0,
                      400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


"""
Define a function to print the metrics
"""


def print_metrics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


""" Read lines from stdin and process them """


try:
    for i, line in enumerate(sys.stdin):
        line = line.strip()

        """ Parse the line and update the metrics """
        parts = line.split()
        if len(parts) != 10:
            continue
        ip_address, _, _, _, _, _, _, _, status_code, file_size = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        """
        Print metrics every 10 lines
        """
        if (i + 1) % 10 == 0:
            print_metrics()


except KeyboardInterrupt:
    """ Handle CTRL+C gracefully by printing the final metrics """
    print_metrics()
