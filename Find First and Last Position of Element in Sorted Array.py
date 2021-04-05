"""
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.res = []
        self.binary_search(nums, 0, len(nums)-1, target)
        if self.res:
            return [min(self.res), max(self.res)]
        return [-1, -1]

    def binary_search(self, nums, start, end, target):
        print(nums, start, end)
        if start==end and nums[start] == target:
            self.res.append(start)
        mid = (start+end)//2
        if start < end:
            if nums[mid] > target:
                self.binary_search(nums, start, mid - 1, target)
            elif nums[mid] < target:
                self.binary_search(nums, mid+1, end, target)
            elif nums[mid] == target:
                self.res.append(mid)
                self.binary_search(nums, mid+1, end, target)
                self.binary_search(nums, start, mid - 1, target)


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 7))
