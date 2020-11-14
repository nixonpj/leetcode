# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1.val += l2.val
        if l1.val > 9:
            l1.val = l1.val % 10
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(1)

        if l1.next:
            if l2.next:
                self.addTwoNumbers(l1.next, l2.next)
            else:
                self.addTwoNumbers(l1.next, ListNode(0))
        else:
            if l2.next:
                l1.next = l2.next
        return l1


