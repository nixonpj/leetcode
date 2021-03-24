"""
Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Status: Incomplete. The logic to follow is the same as 2sum but with extra for loop
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 1, len(nums) - 1
        res = []
        nums.sort()
        print(nums)
        while i < k - 1:
            flag = True
            for j in range(i+1, k):
                print([nums[i], nums[j], nums[k]], i, j, k)
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                elif temp_sum > 0:
                    flag = False
                    print("breaking")
                    break
            if flag:
                i += 1
            else:
                k -= 1
        return res


s = Solution()
# print(s.three_sum([-1, 0, 1, 2, -1, -4]))
print(s.three_sum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# print(s.three_sum([3,0,-2,-1,1,2]))