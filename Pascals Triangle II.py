"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        "Recursive solution which is very slow"
        res = [1]*(rowIndex+1)
        if rowIndex <= 1:
            return res
        for i in range(1, len(res)-1):
            temp = self.getRow(rowIndex-1)
            res[i] = temp[i-1] + temp[i]
            # res[i] = self.getRow(rowIndex-1)[i-1] + self.getRow(rowIndex-1)[i]
        return res

    def getRow2(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(1)
            for j in range(len(res)-2, 0, -1):
                res[j] += res[j-1]
        return res

s = Solution()
print(s.getRow2(7))

