"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different
    ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        store_value, store_index = nums[0], (k % n)
        if k == 0:
            return

        if n % k == 0 and k != 1:
            print("yes")
            self.rotate(nums, 1)
            self.rotate(nums, k-1)
        else:
            for _ in range(len(nums)):
                temp = nums[store_index]
                nums[store_index] = store_value
                store_value = temp
                store_index = (store_index + k) % n
                print(nums, store_value, store_index)
        print("final:", nums)


s = Solution()
print(s.rotate([7, -2, 5, 0, 3, 9], 4))
# print(s.rotate([-1, -100, 3, 99], 2))
