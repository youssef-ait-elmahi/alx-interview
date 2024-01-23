#!/usr/bin/python3
import sys
"""This module contains a script that reads
    stdin line by line and computes metrics"""


def print_metrics(total_file_size, status_code_counts):
    """Print the metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


# Initialize variables
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            pass

        try:
            file_size = int(parts[-1])
            total_size += file_size
        except (ValueError, IndexError):
            pass

        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)
finally:
    print_metrics(total_size, status_codes)
