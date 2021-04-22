"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        print(intervals)
        start, end = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i][0] > end:
                res.append([start, end])
                start, end = intervals[i]
            else:
                end = max(end, intervals[i][1])
            i += 1
            print(res, start, end)
        res.append([start, end])

        return res

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[11, 12], [5,19],[13,15],[15,18]]))
# print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10], [19,20]]))
# 1,2  3, 4