from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        print(f"val: {self.val}, left: {self.left}, right: {self.right}")

class Solution:
    result = []
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return self.result
        if root.right:
            return self.levelOrderBottom(root.right)
        if root.left:
            self.result.append([root.left.val, root.right.val])
        self.result.append([root.right.val])
        print(self.result)
        
        



s = Solution()
print(s.levelOrderBottom(TreeNode(1,TreeNode(3),TreeNode(5, TreeNode(1,TreeNode(3),TreeNode(5))))))
print(s.levelOrderBottom(None))