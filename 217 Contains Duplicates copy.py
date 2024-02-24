def containsDuplicate(nums) -> bool: 
    uniques = set()
    for num in nums:
        if num in uniques:
            return True
        uniques.add(num)
    return False

assert(containsDuplicate([1,2,3,1]) is True)
assert(containsDuplicate([1,2,3,4]) is False)
assert(containsDuplicate([1]) is False)

