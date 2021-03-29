"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""
from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 3**(round(log(abs(n), 3))) == n
        



s = Solution()
print(s.isPowerOfThree(243*243))