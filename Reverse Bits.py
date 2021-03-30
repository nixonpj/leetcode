"""
Reverse bits of a given 32 bits unsigned integer.

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 1
        while n:
            a, b = divmod(n, 2**i)
            res += bool(b)*(2**(32-i))
            print(a, b, n, res, i)
            n = n - b
            i +=1
        return res


s = Solution()
print(s.reverseBits(10))