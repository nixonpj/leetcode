from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m+n-1
    while m-1 >= 0 and n-1 >= 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[i] = nums1[m-1]
            m -= 1
        else:
            nums1[i] = nums2[n-1]
            n -= 1
        i -= 1
        print(nums1, nums2)
    if n-1 >= 0:
        nums1[:n] = nums2[:n]
    print(nums1, nums2)



print(merge([0], 0, [2], 1))
