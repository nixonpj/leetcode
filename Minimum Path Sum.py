"""
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp_table = grid

        prev = 0
        for i in range(len(dp_table[0])):
            dp_table[0][i] += prev
            prev = dp_table[0][i]

        prev = 0
        for i in range(len(dp_table)):
            dp_table[i][0] += prev
            prev = dp_table[i][0]

        for i in range(1,len(dp_table)):
            for j in range(1,len(dp_table[0])):
                if dp_table[i-1][j] < dp_table[i][j-1]:
                    dp_table[i][j] += dp_table[i-1][j]
                else:
                    dp_table[i][j] += dp_table[i][j-1]

        return dp_table[-1][-1]


s = Solution()
# print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(s.minPathSum([[1, 2, 3], [4,5,6]]))