"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        seen = set()
        res = []
        spiral_pattern = [(0,1), (1,0), (0,-1), (-1,0)]
        sp = 0
        i, j = (0, 0)
        while len(seen) < (m*n):
            print(res, seen, i, j)
            seen.add((i, j))
            res.append(matrix[i][j])
            _i, _j = spiral_pattern[sp]
            if not self.valid_cell(i + _i, j + _j, seen, m, n):
                sp = (sp + 1) % 4
                _i, _j = spiral_pattern[sp]
            i += _i
            j += _j
        return res


    def valid_cell(self, i, j, seen, m, n):
        if 0 > i or i >= m or 0 > j or j >= n or (i, j) in seen:
            return False
        return True




s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
