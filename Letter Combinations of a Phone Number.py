"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Status: Solved but recursion/DFS took me an hour to figure out
"""
from typing import List

mapping = {"1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
           "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
           "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        self.dfs(digits, "", ans)
        return ans

    def dfs(self, digits, prefix: str, res):
        if len(digits) == 1:
            res.extend([prefix+letter for letter in mapping[digits[0]]])
        if len(digits) > 1:
            for letter in mapping[digits[0]]:
                self.dfs(digits[1:], prefix+letter, res)


s = Solution()
print(s.letterCombinations(""))




