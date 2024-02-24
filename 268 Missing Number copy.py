def missingNumber(nums: list[int]) -> int:
    sum_nums = sum(nums)
    desired_sum = len(nums)*(len(nums)+1)/2
    return desired_sum-sum_nums

assert(missingNumber([3,0,1]) == 2)
assert(missingNumber([1,2,3,4,5]) == 0)
assert(missingNumber([1,2,3,4,5,0]) == 6)

