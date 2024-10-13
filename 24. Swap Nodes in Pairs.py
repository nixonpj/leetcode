
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[val:{self.val}, next: {self.next}]"

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return None
    head.next = deleteDuplicates2(head.val, head.next)
    return head

def deleteDuplicates2(head: int, next: Optional[ListNode]) -> Optional[ListNode]:
    if next == None:
        return None
    if head == next.val:
        return deleteDuplicates2(next.val, next.next)
    else: 
        next.next = deleteDuplicates2(next.val, next.next)
        return next


print(deleteDuplicates(ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))))