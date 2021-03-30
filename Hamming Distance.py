"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        hamming_d = 0
        while n:
            n = n & (n - 1)
            hamming_d += 1
        return hamming_d


s = Solution()
print(s.hammingDistance(1, 4))