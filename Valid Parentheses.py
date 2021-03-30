"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rel = {')': '(', '}': '{', ']': '['}
        for bracket in s:
            print(stack)
            if bracket in ('(', '{', '['):
                stack.append(bracket)
            else:
                if not stack or rel[bracket] != stack.pop():
                    return False
        return not bool(stack)



s = Solution()
print(s.isValid("([])()"))