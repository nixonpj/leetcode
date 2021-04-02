"""
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white,
and blue, respectively.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)

    def quicksort(self, arr, start, end):

        if start <= end:
            print(arr, start, end)
            pivot_pos = self.partition(arr, start, end)
            print(pivot_pos)
            self.quicksort(arr, start, pivot_pos-1)
            self.quicksort(arr, pivot_pos + 1, end)

    def partition(self, arr, start, end):
        pivot = arr[end]
        i, j = start, end-1
        while i <= j:
            if arr[i] < pivot:
                i += 1
            else:
                arr[j], arr[i] = arr[i], arr[j]
                j -= 1
        arr[end], arr[i] = arr[i], arr[end]
        return i


s = Solution()
# print(s.sortColors([2,0,2,1,1,0,1,2,0,1,1,0,2,1,0]))
print(s.sortColors([2,0,2,1,1,0]))
