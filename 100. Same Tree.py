from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    def dfs(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 == None or node2 == None:
            return node1 == node2
        return (node1.val == node2.val) and self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)
        

s = Solution()
print(s.isSameTree(TreeNode(1,TreeNode(3),TreeNode(5)), TreeNode(1,TreeNode(3),TreeNode(5))))
print(s.isSameTree(None, None))