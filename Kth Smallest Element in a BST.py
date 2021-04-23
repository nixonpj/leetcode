"""
Given the root of a binary search tree, and an integer k, return the kth
(1-indexed) smallest element in the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.k = k
        self.traverse_tree(root)
        return self.res

    def traverse_tree(self, node: TreeNode):
        # print("----", node, "//", self.k, self.res)
        if node and self.k > 0:
            if node.left:
                self.traverse_tree(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            if node.right:
                self.traverse_tree(node.right)



