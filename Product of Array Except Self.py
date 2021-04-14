"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pr = 1
        nums_c = nums[:]
        for i, num in enumerate(nums):
            nums_c[i] = pr
            pr *= num
        pr = 1
        print(nums_c, nums)
        for i in range(n-1, -1, -1):
            nums_c[i] *= pr
            pr *= nums[i]
        return nums_c


s = Solution()
# print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([-1,0]))
