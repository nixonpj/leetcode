"""
Given a collection of numbers, nums, that might contain duplicates, return
all possible unique permutations in any order.

Status: Complete but DFS in current form not the most efficient.
Go through unique nums not all nums in the array
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums and path not in res:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


s = Solution()
print(s.permuteUnique([1,1,2,2]))
