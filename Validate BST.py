from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_BST_helper(self, root: TreeNode):
        res = []
        if root:
            res = self.is_valid_BST_helper(root.left)
            res.append(root.val)
            res = res + self.is_valid_BST_helper(root.right)
        return res

    def isValidBST(self, root: TreeNode) -> bool:
        res = self.is_valid_BST_helper(root)
        return res == sorted(res) and len(set(res)) == len(res)





t4 = TreeNode(12, None, None)
t5 = TreeNode(18, None, None)
t2 = TreeNode(4, None, None)
t3 = TreeNode(16, t4, t5)
t1 = TreeNode(10, t2, t3)
s = Solution()
print(s.is_valid_BST(t3))
