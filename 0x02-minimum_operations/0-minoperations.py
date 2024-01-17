#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i + minOperations(n//i)
        return n
