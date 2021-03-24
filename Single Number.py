"""
Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity
and without using extra memory?

4,4,9,1,1,7,7
Ideas:
Sort array and then find an element with no equal neighbour
Linear scan with hashtable check

Status: Correct, but theres a neater way with XOR (^) operations requiring O(1) space
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        return seen.pop()

s = Solution()
print(s.singleNumber([4,1,2,1,2]))