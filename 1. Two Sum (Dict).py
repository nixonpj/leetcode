def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = dict(nums)
    for index_1, num_1 in d.items():
        num_2 = target - num_1
        if num_2 in nums[index_1 + 1:]:
            pass


# print(twoSum([1, 2, 3, 4, 9], 10) == [0, 4])
# print(twoSum([1, 3, 3], 6) == [1, 2])
# print(twoSum([1, 2, 3, 4], 6) == [1, 3])

a = [1,2,3]
print(dict(a))

