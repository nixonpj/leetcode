"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.
"""
from typing import List
from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        even = (n1 + n2) % 2 == 0
        nums1.append(inf)
        nums2.append(inf)
        new_array = []
        i, j = 0, 0
        while i+j < ((n1 + n2)/2)+1:
            print(i, j, nums1[i], nums2[j], new_array, even)
            if nums1[i] < nums2[j]:
                new_array.append(nums1[i])
                i += 1
            else:
                new_array.append(nums2[j])
                j += 1
        print(new_array)
        if even:
            return (new_array[-1] + new_array[-2])/2
        return new_array[-2]




s = Solution()
print(s.findMedianSortedArrays(nums1=[1, 3, 4, 9, 10], nums2=[2,2,3,5]))
