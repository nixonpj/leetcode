"""
Given a non-empty array nums containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.

Status: Incomplete
"""
from typing import List
from time import time

a = time()

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        print(sum(nums), len(nums))
        self.target_sum = sum(nums) / 2
        self.memo = set()
        if self.target_sum % 1 > 0:
            return False
        self.res = []
        return self.dfs_search(nums[:], [], 0, self.target_sum)

    def dfs_search(self, nums, prefix, prefix_sum, target_sum):
        # print(nums, prefix, prefix_sum, target_sum, self.memo)
        self.memo.add(str(nums))
        if not target_sum:
            # print("hurrah", prefix)
            return True
        if target_sum < 0:
            return False
        # elif sum(prefix) > self.target_sum:
        #     return False
        for i, num in enumerate(nums):
            if str(prefix+[num]) not in self.memo:
                if self.dfs_search(nums[i+1:], prefix+[num], prefix_sum+num, target_sum-num):
                    return True


s = Solution()
# print(s.canPartition([1,5,11,5]))
# print(s.canPartition([100 for _ in range(99)]))
print(time()-a)
print(s.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))
