"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line
i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a
container, such that the container contains the most water.

Notice that you may not slant the container.

Idea: You want the maximum product of two numbers

[1, 8, 6, 2, 5, 4, 8, 3, 7]
[0, 1, 6, 4, 15, 16, 40, 18, 49]
"""
from typing import List


class Solution:
    def maxArea2(self, height: List[int]) -> int:
        """ This is O(n^2) which is timing out on leetcode"""
        res = 0
        max_area_array = [0] * len(height)
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[:i]):
                max_area_array[i] = max(min(h1, h2) * (i - j), max_area_array[i])
        return max(max_area_array)

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i != j:
            h_i = height[i]
            h_j = height[j]
            if h_i > h_j:
                max_area = max(max_area, h_j * (j - i))
                j -= 1
            else:
                max_area = max(max_area, h_i * (j - i))
                i += 1
        return max_area



s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([9, 10, 10, 10, 10, ]))
