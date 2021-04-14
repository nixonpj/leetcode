"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        root.height = 1
        print(root)

    def mark_height(self, node: TreeNode, height):
        node.height = height
        if node.left:
            self.mark_height(node.left, height + 1)
        if node.right:
            self.mark_height(node.right, height + 1)


