#!/usr/bin/python3
""" interview script """
import sys
from collections import defaultdict

""" possibe codes """
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

""" variables for metrics """
total_file_size = 0
lines_by_status_code = defaultdict(int)
lines_processed = 0


try:
    """ Read lines from stdin """
    for line in sys.stdin:
        """ Parse line using regex """
        match = re.match
        (r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line)
        if match:
            """ Extract status code and file size from match """
            status_code = int(match.group(1))
            file_size = int(match.group(2))
            """ Update metrics """
            total_file_size += file_size
            lines_by_status_code[status_code] += 1
            lines_processed += 1
        else:
            """ Skip line if it doesn't match expected format """
            continue

        """ Print metrics every 10 lines """
        if lines_processed % 10 == 0:
            """ Print total file size """
            print(f"File size: {total_file_size}")
            """ Print lines by status code """
            for code in status_codes:
                if lines_by_status_code[code] > 0:
                    print(f"{code}: {lines_by_status_code[code]}")


except KeyboardInterrupt:
    """ Handle keyboard interruption (CTRL + C) """
    """ Print final metrics before exiting """
    print(f"File size: {total_file_size}")
    for code in status_codes:
        """ print out """
        if lines_by_status_code[code] > 0:
            print(f"{code}: {lines_by_status_code[code]}")
