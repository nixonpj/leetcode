"""
Given an integer array nums, find a contiguous non-empty subarray within the
array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
from typing import List
from math import inf


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        dp_arr = [-inf]*len(nums)
        dp_arr[0] = nums[0]
        for i, num in enumerate(nums[1:]):
            if dp_arr[i] != 0:
                dp_arr[i+1] = max(num, num*dp_arr[i])
            else:
                dp_arr[i + 1] = num
            print(dp_arr)
        return max(dp_arr)


s = Solution()
print(s.maxProduct([-2,0,-1,-2,-3]))

