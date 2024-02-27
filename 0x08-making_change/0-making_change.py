#!/usr/bin/python3
def makeChange(coins, total):
    """making change for a given total using the fewest number of coins"""

    if total <= 0:
        return 0
    
    else:
        dp = [float('inf')] * (total + 1)
        dp[0] = 0

        """Build the dp table"""
        for i in range(len(coins)):
            for j in range(coins[i], total + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        """Return the result"""
        return dp[total] if dp[total] != float('inf') else -1
