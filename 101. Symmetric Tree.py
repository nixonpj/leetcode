# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 == None or node2 == None:
            return node1 == node2
        return (node1.val == node2.val) and self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)



s = Solution()
print(s.isSymmetric(TreeNode(1,
                             TreeNode(3, TreeNode(5), TreeNode(2, None, TreeNode(9))),
                             TreeNode(3, TreeNode(2, TreeNode(9)), TreeNode(5)))))
print(s.isSymmetric(None))
        