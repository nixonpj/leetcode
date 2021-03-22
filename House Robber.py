"""
You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = nums[0]
        prev1 = 0
        prev2 = 0
        for num in nums:
            curr = max(num, prev1, prev2 + num)
            res = max(res, curr)
            prev2 = prev1
            prev1 = curr
        return res


a = [1, 2, 3, 1]
b = [2, 7, 9, 3, 1]
c = [1, 2, 3, 1, 2, 7, 9, 3, 1]
"1, 2, 4, 3, 6, "
s = Solution()
print(s.rob(c))
