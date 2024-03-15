#!/usr/bin/python3
"""
define is winner function that takes in two arguments
"""


def getPrimes(n):
    """ list of primes"""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
        define winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_count = ben_count = 0
    for i in range(x):
        prime = getPrimes(nums[i])
        if len(prime) % 2 == 0:
            ben_count += 1
        else:
            maria_count += 1
    if maria_count > ben_count:
        return 'Maria'
    elif ben_count > maria_count:
        return 'Ben'
    return None
