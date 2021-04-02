"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp_array = [[1]*n for _ in range(m)]
        print(dp_array)
        for i, row in enumerate(dp_array[1:]):
            for j, col in enumerate(row[1:]):
                dp_array[i+1][j+1] = dp_array[i][j+1] + dp_array[i+1][j]
        print(dp_array)
        return dp_array[-1][-1]



s = Solution()
print(s.uniquePaths(3, 7))
