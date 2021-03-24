"""
Given the root of a binary tree and an integer targetSum, return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.dfs_visit(root, 0, targetSum)


    def dfs_visit(self, node, cum_sum, target):
        if not node:
            return False
        cum_sum += node.val
        if not node.left and not node.right:
            if cum_sum == target:
                return True
        else:
            return self.dfs_visit(node.left, cum_sum, target) or self.dfs_visit(node.right, cum_sum, target)


t4 = TreeNode(7, None, None)
t5 = TreeNode(4, None, None)
t2 = TreeNode(3, t4, None)
t3 = TreeNode(2, t5, None)
t1 = TreeNode(1, t2, t3)
s = Solution()
print(s.hasPathSum(t1, 7))