
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            try:
                counts[char] = counts[char] - 1
            except KeyError:
                return False
        res = {k : v for k, v in counts.items() if v!=0}
        if not res:
            return True
        return False


s = Solution()
print(s.isAnagram("anagram", "nagaraam"))
