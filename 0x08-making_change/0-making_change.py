#!/usr/bin/python3
'''
function to solve coin change problem
'''


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Parameters:
        coins (list): A list of integers representing the
        denominations of coins available.
        total (int): The total amount to be achieved using the coins.

    Returns:
        int: The fewest number of coins needed to achieve the total amount.
             - If the total is 0 or less, returns 0 (no coins needed).
             - If the total cannot be met using the given coins, returns -1.

    Algorithm:
        - This function uses dynamic programming to solve the problem.
        - It initializes a dp array where dp[i] represents
        the minimum number of coins needed to achieve the amount i.
        - It iteratively updates dp values based on the coin denominations and
        the previous results in the dp array.

    Time Complexity: O(total * len(coins))
    Space Complexity: O(total)
    """
    if total <= 0:
        return 0

    # initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # return the result
    return dp[total] if dp[total] != float('inf') else -1
