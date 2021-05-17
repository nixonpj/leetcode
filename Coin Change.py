"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List
from math import inf


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp_arr = [inf]*(amount+1)
        dp_arr[0] = 0
        print(dp_arr)
        for coin in coins:
            for amt in range(coin, amount+1):
                dp_arr[amt] = min(dp_arr[amt], dp_arr[amt-coin]+1)
                print(coin, amt, dp_arr)
        if dp_arr[-1] == inf:
            return -1
        return dp_arr[-1]


s = Solution()
print(s.coinChange([3, 2, 5], 15))
