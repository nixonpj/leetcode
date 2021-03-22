"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = 0
        curr = nums[0]
        for num in nums:
            curr = max(num, prev + num)
            res = max(res, curr)
            prev = curr
        return res


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
b = [1]
c = [5, 4, -1, 7, 8]
d = [-11, -2, -3, -4]
s = Solution()
print(s.maxSubArray(d))
