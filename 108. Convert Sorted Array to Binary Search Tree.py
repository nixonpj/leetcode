# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"[val:{self.val}, left: {self.left}, right: {self.right}]"

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == None or len(nums) == 0:
            return None
        num_len: int = len(nums)
        if num_len == 1:
            return TreeNode(nums[0])
        return TreeNode(nums[num_len//2], self.sortedArrayToBST(nums[:num_len//2]), self.sortedArrayToBST(nums[num_len//2+1:]))
   
s = Solution()
print(s.sortedArrayToBST([0,1,2,3,4]))
print(s.sortedArrayToBST(None))