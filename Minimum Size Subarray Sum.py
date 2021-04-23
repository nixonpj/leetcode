"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
numsr-1, numsr] of which the sum is greater than or equal to target. If there
is no such subarray, return 0 instead.
"""
from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        res = inf
        t_sum = nums[i]
        while j < len(nums) and res > 1:
            if t_sum >= target:
                res = min(res, j - i + 1)
                t_sum -= nums[i]
                i += 1
            else:
                j += 1
                if j >= len(nums):
                    break
                t_sum += nums[j]
        return res if res is not inf else 0


