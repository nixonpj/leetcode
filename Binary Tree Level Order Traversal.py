"""
Given the root of a binary tree, return the level order traversal of its
nodes' values. (i.e., from left to right, level by level).
"""


# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        que = deque()
        heights = {}
        height = 0
        if not root:
            return []

        que.append((root, height + 1))
        while que:
            node, height = que.popleft()
            # print(node.val, height, heights)
            heights.setdefault(height, []).append(node.val)
            if node.left:
                que.append((node.left, height + 1))
            if node.right:
                que.append((node.right, height + 1))
        return heights.values()

