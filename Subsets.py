"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """This gives all combinations. You only need permutations."""
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums: List, prefix: List):
        print(nums, prefix, self.res)
        if prefix not in self.res:
            self.res.extend([prefix])
        if nums not in self.res:
            self.res.extend([nums])
        # if len(nums) == 1:
        #     for num in nums:
        #         if [prefix+[num]] not in self.res:
        #             self.res.extend([prefix+[num]])
        if len(nums) >= 1:
            for i, num in enumerate(nums):
                self.dfs(nums[i+1:], prefix+[num])  # Removing this from the call "nums[:i]+" worked partially




s = Solution()
print(s.subsets([1,2,3]))