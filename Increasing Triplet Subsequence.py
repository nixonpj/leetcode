"""
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.
"""
from typing import List
from math import inf


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest_one = nums[0]
        lowest_two = inf
        for i, num in enumerate(nums):
            print(i, num, lowest_one, lowest_two)
            if lowest_two is not None and num > lowest_two:
                return True
            if num > lowest_one:
                lowest_two = min(lowest_two, num)
            else:
                lowest_one = min(lowest_one, num)
        return False

s = Solution()
# print(s.increasingTriplet([5,4,3,7,2,1,9]))
print(s.increasingTriplet([1,0,0,-1,0,100]))
