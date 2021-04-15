"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        height = 0
        if not root:
            return height
        que = deque()
        que.append((root, height+1))
        while que:
            node = que.popleft()
            if node.left:
                que.append((node.left, height+1))
            if node.right:
                que.append((node.right, height+1))
            if not node.left and not node.right:
                return height



