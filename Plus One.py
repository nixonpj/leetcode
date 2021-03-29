"""
Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1
        for i in range(len(digits)-1):
            if digits[n-1-i] == 10:
                digits[n-1-i] = 0
                digits[n-1-i-1] += 1
        if digits[0] == 10:
            return [1, 0] + digits[1:]

        return digits

s = Solution()
print(s.plusOne([9,8,9,9]))
