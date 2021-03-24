"""
Given a string s, return the longest palindromic substring in s.
1st letter is a palindrom
2nd letter
"""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        seen = {}
        res_n = 0
        res_word = s[0]
        for index, char in enumerate(s):
            seen[char] = seen.get(char, []) + [index]
            for start_index in seen[char]:
                print(start_index, seen[char])
                if self.is_palindrome(s[start_index:index+1]):
                    if (index-start_index)>res_n:
                        res_n = index-start_index
                        res_word = s[start_index:index+1]
                    break
        print(seen)
        return res_word

    def is_palindrome(self, word):
        n = len(word)
        for i in range(n//2):
            if word[i]!=word[n-1-i]:
                return False
        return True


s = Solution()
print(s.longest_palindrome("aaaaaaaaaaaaaa"))
