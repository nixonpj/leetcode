"""
Given the root of a binary tree, return the average value of the
nodes on each level in the form of an array. Answers within 10-5
of the actual answer will be accepted.
"""
from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = {}
        que = deque([])
        que.append((0, root))
        while que:
            level, node = que.popleft()
            level_sum, level_num = levels.get(level, (0, 0))
            levels[level] = level_sum + node.val, level_num + 1
            if node.left:
                que.append([level + 1, node.left])
            if node.right:
                que.append([level + 1, node.right])

        return list(map(lambda tup: tup[0]/tup[1],levels.values()))
