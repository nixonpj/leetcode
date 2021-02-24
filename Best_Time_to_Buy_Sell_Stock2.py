from typing import List


def max_profit(prices: List[int]) -> int:
    """
    This is a O(n^2) DP solution
    :param prices:
    :return:
    """
    n = len(prices)
    profits_dp = [0] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            profits_dp[i] = max((prices[i] - prices[j]) + profits_dp[j], profits_dp[i - 1], profits_dp[i])
            if profits_dp[j] <= profits_dp[i]:
                break

    return int(profits_dp[-1])


def max_profit_quick(prices: List[int]) -> int:
    """
    This is a O(n) solution
    :param prices:
    :return:
    """
    buy, sell, profit = prices[0], prices[0], 0
    n = len(prices)
    for i in range(1, n - 1):
        if prices[i - 1] >= prices[i] <= prices[i + 1]:  # Look for local minima to buy
            buy = prices[i]
        elif prices[i - 1] <= prices[i] >= prices[i + 1]:  # Look for local maxima to sell
            sell = prices[i]
            if buy is not None:
                profit += (sell - buy)
                buy = None
    if prices[n - 1] > prices[n - 2]:  # Check if last price to be sold at
        sell = prices[n - 1]
        profit += (sell - buy)
    return profit


# print(max_profit_quick([7, 1, 17, 7, 1, 5, 3, 6, 4]))
print(max_profit_quick([5, 2, 3, 2, 6, 6, 2, 9, 1, 0, 7, 4, 5, 0]))
