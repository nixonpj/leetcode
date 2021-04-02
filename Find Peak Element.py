"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞
"""
from typing import List
from math import inf


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 1 and nums[0] > nums[1]:
            return 0
        if n > 1 and nums[-1] > nums[-2]:
            return n-1
        for i, num in enumerate(nums[1:-1]):
            if nums[i] < num > nums[i+2]:
                return i+1



s = Solution()
print(s.findPeakElement([2,10,4]))


