"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""
import re, string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_str = re.sub(r'[^a-zA-Z0-9]+', '', s.lower())
        print(valid_str)
        return self.validPalindrome(valid_str)

    def validPalindrome(self, s):
        if len(s) < 2:
            return True
        return (s[0]==s[-1]) and self.validPalindrome(s[1:-1])


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("ab_a"))