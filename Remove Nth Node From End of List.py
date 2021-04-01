"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
Status: Incomplete
"""
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
        node = head
        q = deque(maxlen=n + 2)
        while node:
            q.append(node)
            node = node.next
        q.append(None)
        if len(q) < (n + 2):
            return head.next
        q[0].next = q[2]
        return head


s = Solution()
