"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_ht = {}
        for num in nums:
            counts_ht[num] = counts_ht.get(num, 0) + 1
        print(counts_ht)
        return  [k for v, k in sorted(((v, k) for k, v in counts_ht.items()), reverse=True)[:k]]


s = Solution()
print(s.topKFrequent([111,111,111,12,12,13], 2))