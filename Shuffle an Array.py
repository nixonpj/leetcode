import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self._nums = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled_nums = []
        nums = self._nums[:]
        i = len(nums)
        while i > 0:
            random_pick = random.randint(0, i-1)
            nums[random_pick], nums[-1] = nums[-1], nums[random_pick]
            shuffled_nums.append(nums.pop())
            i-=1
            # print(random_pick, shuffled_nums, nums)
        return shuffled_nums





# Your Solution object will be instantiated and called as such:
nums = [1,2,3,4]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)