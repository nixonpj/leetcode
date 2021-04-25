"""
Given an array of integers nums containing n + 1 integers where each
integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = {i for i in range(1, len(nums))}
        print(numbers)

        for num in nums:
            try:
                numbers.remove(num)
            except KeyError:
                return num


s = Solution()
# print(s.findDuplicate([1,3,4,2,2]))
print(s.findDuplicate([3,1,3,4,2]))
