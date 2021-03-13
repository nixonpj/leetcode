class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in s:
            if counts[char] == 1:
                return s.index(char)
        return -1


s = Solution()
print(s.firstUniqChar("aadadaad"))
