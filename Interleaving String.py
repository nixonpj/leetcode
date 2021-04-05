"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into
non-empty substrings such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
Status: Incomplete. Looks like a DP problem but unable to frame the problem
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i, j = 0, 0
        n1, n2 = len(s1), len(s2)
        l = 0
        while i < n1 and j < n2:
            if s1[i] == s2[j] == s3[l]:
                break
            elif s1[i] == s3[l]:
                i += 1
            elif s2[j] == s3[l]:
                j += 1
            else:
                return False
            l += 1
        print(i, j, l)
        n1, n2 = len(s1)-1, len(s2)-1
        m = len(s3)-1
        while n1 > 0 and n2 > 0:
            if s1[n1] == s2[n2] == s3[m]:
                break
            elif s1[n1] == s3[m]:
                n1 -= 1
            elif s2[n2] == s3[m]:
                n2 -= 1
            else:
                return False
            m -= 1
        print(n1, n2, m)

        res = 0
        for letter in s1[i:n1+1]+s2[j:n2+1]+s3[l:m+1]:
            res = res ^ ord(letter)
        return not res

s = Solution()
# print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))