"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Status: Incomplete
"""
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp_dict = {coin: {} for coin in coins}
        print(dp_dict)
        for coin in coins:
            for amt in range(0, amount+1, coin):
                if amt % coin == 0 and ((amount-amt) > coin or (amount-amt) in dp_dict):
                    dp_dict[coin][amt] = amt // coin
        return dp_dict


s = Solution()
print(s.coinChange([3, 2, 5], 11))
