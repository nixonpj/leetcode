"""
Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """ Works but slow and memory intensive"""
        set_of_nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in set_of_nums:
                return i

        # _min, _max, n = min(nums), max(nums), len(nums)
        # if _min > 1 or _max < 1:
        #     return 1
        # if _max - _min == n - 1:
        #     return _max + 1





s = Solution()
# print(s.firstMissingPositive([7,8,9,11,12]))
print(s.firstMissingPositive([1,2,3,4,5,7]))
print(s.firstMissingPositive([-4,-2,-9]))
