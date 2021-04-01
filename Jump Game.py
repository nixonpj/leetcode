"""
Given an array of non-negative integers nums, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Status: Passing 74/75 tests with 1 TLE on reverse sorted array
"""
from typing import List


class Solution:
    def canJump2(self, nums: List[int]) -> bool:
        """ TLE """
        stack = [0]
        seen = {0}
        # unseen = set(range(n))
        n = len(nums) - 1
        if not n:
            return True
        while stack:
            index = stack.pop()
            if index + nums[index%n] >= n:
                return True
            print(set(range(index, index+nums[index]+1)).difference(seen), seen, stack)
            for jump_dist in set(range(index, index+nums[index]+1)).difference(seen):
                print(index, nums[index], jump_dist, index+jump_dist)
                if jump_dist not in seen:
                    stack.append(jump_dist)
                    seen.add(jump_dist)
        return False

    def canJump(self, nums: List[int]) -> bool:
        """Works great!"""
        dp_arr = nums[:]
        max_reachable = 0
        for i, num in enumerate(nums):
            if max_reachable >= i:
                dp_arr[i] = i + num
                max_reachable = max(max_reachable, dp_arr[i])
            else:
                return False
        return True


s = Solution()
print(s.canJump([10, 9, 8, 7, 6,5,4,3,2,1,0,0]))
# print(s.canJump2([2,3,1,1,4,1,2,5,1,2,1,2,1,2,1,0,0,1,1,2,3,5]))
