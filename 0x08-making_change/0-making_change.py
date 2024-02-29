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
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
