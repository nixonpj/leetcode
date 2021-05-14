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
        first_house = nums[0]
        if len(nums) == 1:
            return first_house
        second_house = max(nums[0], nums[1])
        res = max(first_house, second_house)
        for house in range(2, len(nums)):
            temp = max(second_house,first_house+nums[house])
            first_house, second_house = second_house, temp
            res = max(res, temp)

        return res


a = [1, 2, 3, 1]
b = [2, 7, 9, 3, 1]
c = [1, 2, 3, 1, 2, 7, 9, 3, 1]
"1, 2, 4, 3, 6, "
s = Solution()
print(s.rob(c))




