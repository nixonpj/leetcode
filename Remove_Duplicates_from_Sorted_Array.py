from typing import List


def remove_duplicates(nums: List[int]) -> int:
    unique = 0
    seen = None
    for num in nums:
        if num != seen:
            seen = num
            nums[unique] = num
            unique += 1
    return unique


print(remove_duplicates([1, 1, 1, 2, 2, 3]))
