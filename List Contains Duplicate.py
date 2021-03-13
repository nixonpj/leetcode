from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


s = Solution()
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(s.containsDuplicate([1, 2, 3, 1]))

print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
