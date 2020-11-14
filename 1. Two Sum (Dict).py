def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
        num_2 = target - num
        if num_2 in d:
            return [d[num_2], i]
        else:
            d[num] = i


print(twoSum([1, 2, 3, 4, 9], 10) == [0, 4])
print(twoSum([1, 3, 3], 6) == [1, 2])
print(twoSum([1, 2, 3, 4], 6) == [1, 3])



