"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity?
"""
from typing import List
from math import inf


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_, max_ = inf, -inf
        for num in nums:
            min_ = min(min_, num)
            max_ = max(max_, num)
        if min_:
            return 0
        print(max_*(max_+1)/2, (min_*(min_-1)),  sum(nums))
        ans = int((max_*(max_+1)/2) - (min_*(min_-1)/2) - sum(nums))
        if ans:
            return ans
        return max_ + 1


s = Solution()
print(s.missingNumber([1,2,4]))