"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1],
we split the array into some number of "chunks" (partitions), and individually
sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)
        print(n, arr, arr.index(n-1))
        try:
            if arr.index(n-1) == 0:
                return 1
        except ValueError:
            return 0
        return 1 + self.maxChunksToSorted(arr[:arr.index(n-1)])
        # count = 0
        # for i, num in enumerate(arr):
        #     if num:


s = Solution()
# print(s.maxChunksToSorted([4,3,2,1,5,6,7]))
# print(s.maxChunksToSorted([4,3,2,1,0,5]))
print(s.maxChunksToSorted([4, 7, 5, 2, 0, 1, 6, 3]))



