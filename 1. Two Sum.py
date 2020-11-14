def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for index_1, num1 in enumerate(nums):
        num2 = target - num1
        if num2 in nums[index_1 + 1:]:
            return [index_1, nums[index_1 + 1:].index(num2) + index_1 + 1]


print(twoSum([1, 2, 3, 4, 9], 10) == [0, 4])
print(twoSum([1, 3, 3], 6) == [1, 2])
print(twoSum([1, 2, 3, 4], 6) == [1, 3])

