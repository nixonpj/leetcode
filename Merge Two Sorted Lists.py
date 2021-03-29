"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the
first two lists.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []

        while True:
            try:
                if l1.val > l2.val:
                    res.append(l1.val)
                    l1 = l1.next
                else:
                    res.append(l2.val)
                    l2 = l2.next
            except IndexError:
                pass
        return res



