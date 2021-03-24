"""
Given an input string (s) and a pattern (p), implement regular expression matching with support
for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Idea: Start from the end and backtrack

Code is too long and inefficient. Optimize next time
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        patterns = [self.judge_char_type(p, i) for i in range(len(p)) if self.judge_char_type(p, i)]
        dp_table = [[self.match(letter, pattern) for letter in s] for pattern in patterns]
        print(patterns, dp_table)
        if len(s) == 0:
            return all([ptrn[1] for ptrn in patterns])
        if len(patterns) == 0:
            return False
        return self.backtrack(dp_table, s, patterns)

    def backtrack(self, dp_table, string, patterns):
        pattern_i = len(dp_table) - 1
        string_i = len(dp_table[0]) - 1
        # stack = [dp_table[pattern_i][string_i]]
        stack = [(pattern_i, string_i)]

        # Logic below incomplete. Restart here:
        while stack:
            p_i, s_i = stack.pop()

            pattern = patterns[p_i]
            letter = string[s_i]
            matched = dp_table[p_i][s_i]
            print(p_i, s_i, pattern, letter, matched, stack)
            if matched:
                if p_i == s_i == 0:
                    return True
                if s_i == 0:
                    if all([ptrn[1] for ptrn in patterns[:p_i]]):
                        return True
                if p_i > 0 and s_i > 0:  # If match you can definitely move diagonally top left
                    stack.append((p_i - 1, s_i - 1))
                if pattern[1]:  # If repeatable then add top and left moves
                    if p_i > 0:
                        stack.append((p_i - 1, s_i))
                    if s_i > 0:
                        stack.append((p_i, s_i - 1))
            else:
                if pattern[1]:
                    if p_i > 0:
                        stack.append((p_i - 1, s_i))
        return False

    def match(self, s, p):
        if p[2]:
            return True
        return s == p[0]

    def judge_char_type(self, word, i):
        repeatable, wildcard = False, False
        if word[i] == '*':
            return None
        if i != len(word) - 1:
            repeatable = (word[i + 1] == '*')
        wildcard = (word[i] == '.')
        return word[i], repeatable, wildcard


s = Solution()
# print(s.isMatch("mississippi", "mis*is*p*."))
print(s.isMatch("", ""))
