"""
You are given two integer arrays nums1 and nums2 sorted in ascending
order and an integer k.

Define a pair (u, v) which consists of one element from the first array
and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Status: Incomplete
"""
from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []

        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(res, [num1+num2, num1, num2])
        return list(map(lambda x: x[1:], res))


s = Solution()
print(s.kSmallestPairs([1,1,2], [1,2,3], 3))
