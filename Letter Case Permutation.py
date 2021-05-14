"""
Given a string s, we can transform every letter individually to be lowercase or uppercase
to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        self.dfs("", s[0], s[1:])
        return self.res

    def dfs(self, prefix, letter, rest):
        # print(prefix, "-", letter, "-", rest)
        if not rest:
            if letter.isnumeric():
                self.res.append(prefix + letter)
            else:
                self.res.append(prefix + letter.upper())
                self.res.append(prefix + letter.lower())
        else:
            if letter.isnumeric():
                self.dfs(prefix + letter, rest[0], rest[1:])
            else:
                self.dfs(prefix + letter.upper(), rest[0], rest[1:])
                self.dfs(prefix + letter.lower(), rest[0], rest[1:])




s = Solution()
print(s.letterCasePermutation("abc"))

