from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    store_value, store_index = nums[0], (k % n)

    for _ in range(len(nums)):
        temp = nums[store_index]
        nums[store_index] = store_value
        store_value = temp
        store_index = (store_index + k) % n
        print(nums)


# print(rotate([7, -2, 5, 0, 3], 13))
print(rotate([-1, -100, 3, 99], 2))
