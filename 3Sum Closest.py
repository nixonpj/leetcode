"""
Given an array nums of n integers and an integer target, find three integers
in nums such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""
from typing import List
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        i, k = 0, len(nums)-1
        best_sum = inf
        while i + 1 < k:
            sum2 = nums[i]+nums[k]
            best_2sum = inf
            for num in nums[i+1:k]:
                if abs((sum2 + num)-target) < abs(best_2sum-target):
                    best_2sum = sum2 + num
                print(nums[i], num, nums[k], best_sum, best_2sum)
            if abs(best_2sum-target) < abs(best_sum-target):
                best_sum = best_2sum
            if best_2sum < target:
                i += 1
            else:
                k -= 1
            print("----")


        return best_sum


s = Solution()
print(s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
# print(s.threeSumClosest([-4,1,-1,2], 1))

