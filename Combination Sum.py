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
        dp_array = [0] + [-inf]*len(candidates)

        for i, cand in enumerate(candidates):
            for t in range(1, target+1):
                if t >= cand:
                    dp_array[t] += (t % cand)


s = Solution()
print(s.combinationSum([2,3,6,7], 7))

