"""
Given an array of distinct integers candidates and a target integer target, return a
list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations
are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less
than 150 combinations for the given input.

Status: Interesting Problem. Come back to this when you're sharper.
"""
from typing import List
from math import inf


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(candidates, [], 0, target)
        return self.res

    def dfs(self, nums, path, path_sum, target):
        if path_sum == target:
            self.res.append(path)
        if path_sum < target:
            for i, num in enumerate(nums):
                self.dfs(nums[i:], path+[num], path_sum+num, target)


s = Solution()
print(s.combinationSum([2,3,6,7], 7))

