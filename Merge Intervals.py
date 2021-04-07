"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

#Status: Incomplete
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starting_times = sorted([interval[0] for interval in intervals])
        ending_times = sorted([interval[1] for interval in intervals])

        print(starting_times, ending_times)

        res = []
        s_i, e_i = 0, 0

        start_time = starting_times[0]
        while s_i < len(starting_times):
            if ending_times[e_i] < starting_times[s_i]:
                s_i += 1

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
