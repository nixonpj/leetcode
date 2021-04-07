"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

A leaf node is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.pre_order_traversal(root, "")
        return self.sum

    def pre_order_traversal(self, node: TreeNode, prefix):
        if not (node.left or node.right):
            self.sum += int(prefix+str(node.val))
        else:
            if node.left:
                self.pre_order_traversal(node.left, prefix + str(node.val))
            if node.right:
                self.pre_order_traversal(node.right, prefix + str(node.val))

