"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
from typing import List
from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ Very slow"""
        self.quicksort(nums, 0, len(nums) - 1, k-1)
        return nums[k-1]

    def quicksort(self, nums, start, end, k):
        if start < end:
            print(nums, start, end)
            pivot_pos = self.partition(nums, start, end)
            print(pivot_pos)
            if pivot_pos == k:
                return pivot_pos
            if start <= k <= pivot_pos - 1:
                self.quicksort(nums, start, pivot_pos - 1, k)
            else:
                self.quicksort(nums, pivot_pos + 1, end, k)

    def partition(self, nums, start, end):
        # random_pick = randint(start, end)
        # nums[end], nums[random_pick] = nums[random_pick], nums[end]
        # print(nums[start:end+1])
        i, j = start, end - 1
        while i <= j:
            if nums[i] < nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        nums[end], nums[i] = nums[i], nums[end]
        return i

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        count_ht = {}
        for num in nums:
            count_ht[num] = count_ht.get(num, 0) + 1
        print(count_ht)
        i = 0
        for num in sorted(count_ht.keys(), reverse=True):
            print(i, num, count_ht[num])
            i += count_ht[num]
            if i >= k:
                return num


s = Solution()
print(s.findKthLargest2([3,2,3,1,2,4,5,5,6], 5))
