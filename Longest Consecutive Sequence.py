"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Status: Incomplete. Come back to it later. Using hasttables/set is the correct approach but logic is wrong
and can be simplified
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ht_decreasing = {}
        ht_increasing = {}
        for num in nums:
            if num in ht_decreasing:
                lng = ht_decreasing.pop(num)
                ht_decreasing[num-1] = max(lng+1, ht_decreasing.get(num-1, 1))
            else:
                ht_decreasing[num - 1] = ht_decreasing.get(num-1, 1)
            if num in ht_increasing:
                lng = ht_increasing.pop(num)
                ht_increasing[num+1] = max(lng+1, ht_increasing.get(num-1, 1))
            else:
                ht_increasing[num+1] = ht_increasing.get(num+1, 1)

            print(ht_decreasing, ht_increasing)
        print("----")
        for num in nums[::-1]:
            if num in ht_decreasing:
                lng = ht_decreasing.pop(num)
                ht_decreasing[num-1] = max(lng+1, ht_decreasing.get(num-1, 1))
            else:
                ht_decreasing[num - 1] = ht_decreasing.get(num-1, 0) + 1
            if num in ht_increasing:
                lng = ht_increasing.pop(num)
                ht_increasing[num+1] = max(lng+1, ht_increasing.get(num-1, 1))
            else:
                ht_increasing[num+1] = ht_increasing.get(num+1, 0) + 1

            print(ht_decreasing, ht_increasing)
        return max(max(ht_increasing.values())-1, max(ht_decreasing.values())-1)


s = Solution()
# print(s.longestConsecutive([100,4,200,1,3,2]))
# print(s.longestConsecutive([3,1,7,0,3,6,9]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

