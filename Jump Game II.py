"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""
from typing import List
from math import inf


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp_arr = [0]+([inf]*(len(nums)-1))
        print(dp_arr)
        for i, num in enumerate(nums):
            for jump_length in range(1,num+1):
                try:
                    dp_arr[i+jump_length] = min(dp_arr[i+jump_length], dp_arr[i] + 1)
                except IndexError:
                    break
        print(dp_arr)
        return dp_arr[-1]


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
