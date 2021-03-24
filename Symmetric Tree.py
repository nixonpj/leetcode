"""Incomplete"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        nodes = []

        def inorder_traversal(root_: TreeNode):
            if root_:
                print(root_.val, nodes)
                inorder_traversal(root_.left)
                nodes.append(root_.val)
                inorder_traversal(root_.right)
            else:
                nodes.append(None)
            return nodes
        nodes_res = inorder_traversal(root)
        print(nodes_res)

        def symmetric_check(nodes):
            n = len(nodes)
            if len(nodes)%2:
                return False
            for i in range((n // 2)):
                print(i)
                if nodes[i] != nodes[n - 1 - i]:
                    return False
            return True

        return symmetric_check(nodes_res)



t4 = TreeNode(3, None, None)
t5 = TreeNode(3, None, None)
t2 = TreeNode(2, t4, None)
t3 = TreeNode(2, t5, None)
t1 = TreeNode(1, t2, t3)
s = Solution()
print(s.is_symmetric(t1))