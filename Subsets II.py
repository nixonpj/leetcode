"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.dfs(nums, [])
        return list(self.res)

    def dfs(self, nums, prefix):
        print(nums, prefix, self.res)
        if prefix not in self.res:
            self.res.extend([prefix])
        if nums not in self.res:
            self.res.extend([nums])
        for i, num in enumerate(nums):
            self.dfs(nums[i+1:], prefix+[num])


s = Solution()
print(s.subsetsWithDup([1,2,2]))