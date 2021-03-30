"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Status: Incomplete
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows <= 2:
            return res[:numRows]
        for x in range(3, numRows+1):
            row = [1]*x

            res.append(res[x-2])
        return res



s = Solution()
print(s.generate(5))
