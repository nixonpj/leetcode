"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = 1, 1
        res = [1]*len(nums)
        for i, num in enumerate(nums):
            res[i], left_prod = left_prod, left_prod*num

        for j in range(len(nums)-1, -1, -1):
            res[j], right_prod = res[j]*right_prod, right_prod * nums[j]
        return res


s = Solution()
# print(s.productExceptSelf([1,2,3,4]))
# print(s.productExceptSelf([-1,1,0,-3,3]))
print(s.productExceptSelf([-1,0]))
