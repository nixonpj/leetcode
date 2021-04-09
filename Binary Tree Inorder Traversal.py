"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        if not root:
            return self.res
        self.traversal(root)
        return self.res

    def traversal(self, root: TreeNode):
        if root.left:
            self.traversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.traversal(root.right)


s = Solution()

