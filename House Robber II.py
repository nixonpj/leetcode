"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one. Meanwhile,
adjacent houses have a security system connected, and it will automatically contact
the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return
the maximum amount of money you can rob tonight without alerting the police.

Status: Incomplete
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_array = nums[:]
        for house in range(2, n-1):
            dp_array[house] = max(dp_array[house-1], dp_array[house-2]+nums[house])
        print(dp_array)
        return max(dp_array)


a = [1, 2, 3, 1]
b = [2, 7, 9, 3, 1]
c = [1, 2, 3, 1, 2, 7, 9, 3, 1]
s = Solution()
print(s.rob(b))