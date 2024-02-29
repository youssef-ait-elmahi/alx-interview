#!/usr/bin/python3

"""Making change"""


def makeChange(coins, total):
    """
    Given an array of coins and a total amount, return the minimum number
    of coins needed to make up that amount.
    :param coins: list of integers
    :param total: integer
    :return: integer
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
