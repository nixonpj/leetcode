
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
