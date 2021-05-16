"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Status: Not the best possible solution. Come back to it later. Using hasttables/set is the correct approach but logic
is wrong and can be simplified
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        dp_arr = [1] * n
        _max = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                dp_arr[i] = dp_arr[i - 1] + 1
            if nums[i] == nums[i - 1]:
                dp_arr[i] = dp_arr[i - 1]
        return max(dp_arr)


s = Solution()
# print(s.longestConsecutive([100,4,200,1,3,2]))
# print(s.longestConsecutive([3,1,7,0,3,6,9]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

