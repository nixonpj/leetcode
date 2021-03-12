import queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root.val:
        return 0
    depth = 1
    q = queue.Queue()
    q.put((root, depth))
    while not q.empty():

        popped_item, depth_item = q.get()
        print(popped_item.val, popped_item.left, popped_item.right, depth_item, depth)
        depth = max(depth, depth_item)
        if popped_item.left:
            q.put((popped_item.left, depth_item + 1))
        if popped_item.right:
            q.put((popped_item.right, depth_item + 1))
    return depth


t1 = TreeNode(2,None,None)

print(max_depth(t1))
