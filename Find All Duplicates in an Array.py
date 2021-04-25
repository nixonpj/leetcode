"""
Given an integer array nums of length n where all the integers of nums are
in the range [1, n] and each integer appears once or twice, return an array
of all the integers that appears twice.
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numbers = {i for i in range(1, len(nums)+1)}
        print(numbers)
        res = []

        for num in nums:
            try:
                numbers.remove(num)
            except KeyError:
                res.append(num)
        return res



s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))
