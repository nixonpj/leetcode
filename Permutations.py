"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

s = Solution()
print(s.permute([1,2,3,4]))

