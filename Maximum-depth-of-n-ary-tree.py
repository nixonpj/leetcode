"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the
root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.max_depth = 0
        if not root:
            return self.max_depth

        self.stack = []
        self.stack.append((root, 1))
        while self.stack:
            node, height = self.stack.pop()
            self.max_depth = max(self.max_depth, height)
            for child in node.children:
                self.stack.append((child, height + 1))
        return self.max_depth


