def productExceptSelf(nums: list[int]) -> list[int]:
    res = nums.copy()
    product_tracker = 1
    for i, num in enumerate(nums): 
        res[i] = product_tracker
        product_tracker*=num
    product_tracker = 1
    for i, num in enumerate(reversed(nums)): 
        res[len(nums)-1-i]*= product_tracker
        product_tracker*=num
    return res


assert(productExceptSelf([1,2,3,4]) == [24,12,8,6])
assert(productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])
assert(productExceptSelf([5,0]) == [0,5])


