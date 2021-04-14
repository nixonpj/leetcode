"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [], len(nums))
        return self.res

    def dfs(self, nums, prefix, n):
        if nums not in self.res and len(nums)==n:
            self.res.append(nums)
        # if prefix not in self.res and len(prefix)==n:
        #     self.res.append(prefix)
        for i, num in enumerate(nums):
            self.dfs(nums[:i]+nums[i+1:], prefix+[num], n)


s = Solution()
print(s.permute([1,2,3]))

