"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0.
Do it in-place.

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    rows.add(i)
                    cols.add(j)
                    print(rows, cols)

        for i, row in enumerate(matrix):
            if i in rows:
                matrix[i] = [0]*len(row)
            else:
                for j, num in enumerate(row):
                    if j in cols:
                        matrix[i][j] = 0

        return matrix



s = Solution()
print(s.setZeroes([[0,1,2,3],[3,4,5,0],[1,3,1,5]]))
