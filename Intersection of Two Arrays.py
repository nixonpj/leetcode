"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and
 you may return the result in any order.
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_ht = {}   
        for num in nums1:
            count_ht[num] = count_ht.get(num, 0) + 1

        res = []
        for num in nums2:
            if num in count_ht:
                if count_ht[num]>0:
                    res.append(num)
                    count_ht[num] -= 1

        print(count_ht, res)



s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))