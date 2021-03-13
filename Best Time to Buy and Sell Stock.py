from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        profit = 0
        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(price, min_price)
        return profit




s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([4,1,5,8,2,4,9]))

