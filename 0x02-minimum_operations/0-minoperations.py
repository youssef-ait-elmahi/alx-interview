#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    calculates the fewest number of
    operations needed to result in
    """
    if n <= 1:
        return 0
    min_operations = 0
    current_length = 1
    clipboard = 0
    while current_length != n:
        if n % current_length == 0:
            clipboard = current_length
            min_operations += 1
        current_length += clipboard
        min_operations += 1
    return min_operations
