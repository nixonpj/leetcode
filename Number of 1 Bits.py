"""
Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).

Constraints:

    The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        one_count = 0
        i = 1
        n = abs(n)
        while n:
            x = (n % 2 ** i)
            one_count += bool(x)
            print(n, 2 ** i, x, one_count)
            n = n - x
            i += 1
        return one_count


s = Solution()
print(s.hammingWeight(15))

