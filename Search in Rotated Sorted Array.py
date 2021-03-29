"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index
k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7]
might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target
if it is in nums, or -1 if it is not in nums.

Status: Incomplete
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        n = len(nums)
        start = nums[0]
        mid = nums[n//2]
        end = nums[-1]
        if start < mid:
            if start < target < mid:
                return self.search(nums[:(n//2) + 1], target)
            else:
                return n//2 + self.search(nums[(n//2)+1:], target)
        else:
            if mid < target < end:
                return n//2 + self.search(nums[(n//2)+1:], target)
            else:
                return self.search(nums[:(n // 2) + 1], target)



s = Solution()
print(s.search(nums = [4,5,6,7,0,1,2], target = 4))
