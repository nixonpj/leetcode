"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        i = 0
        for j, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                nums[i] = num
                i += 1

        for i in range(zero_count):
            nums[-1-i] = 0




s = Solution()
print(s.moveZeroes([0,1,0,3,12]))