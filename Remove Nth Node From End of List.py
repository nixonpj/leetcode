"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
Status: Incomplete
"""
from queue import Queue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
        node = head
        array_n = []
        i = 0
        while node.next:
            array_n.append = node
            node = node.next
            i += 1
        array_n[i-n].next = array_n[i-n+1].next
        return array_n[i-n]


s = Solution()
