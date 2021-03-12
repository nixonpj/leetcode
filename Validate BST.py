from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_BST2(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val > root.val:
            print("yes")
            return False
        if root.right and root.right.val < root.val:
            print("yesss")
            return False
        return True and self.is_valid_BST(root.left) and self.is_valid_BST(root.right)

    def is_valid_BST3(self, root: TreeNode) -> bool:
            res = []
            if root:
                print(res)
                res = self.is_valid_BST(root.left)
                res.append(root.val)
                res = res + self.is_valid_BST(root.right)
            return res==sorted(res)

    def is_valid_BST(self, root: TreeNode) -> bool:




t4 = TreeNode(12, None, None)
t5 = TreeNode(18, None, None)
t2 = TreeNode(4, None, None)
t3 = TreeNode(16, t4, t5)
t1 = TreeNode(10, t2, t3)
s = Solution()
print(s.is_valid_BST(t3))
