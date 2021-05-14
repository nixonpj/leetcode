"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.dfs(1, n, [], k)
        return self.res

    def dfs(self, start, end, path, k):
        print(start, end, path)
        if len(path) == k:
            self.res.append(path)
        else:
            for i in range(start, end+1):
                self.dfs(i+1, end, path+[i], k)


s = Solution()
print(s.combine(4, 2))
