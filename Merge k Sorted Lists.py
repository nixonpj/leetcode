"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List
from math import inf

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        O(kN)
        """

        res = ListNode(0, None)
        original_pointer = res

        while True:
            min_val, min_index = inf, None
            for i, lst in enumerate(lists):
                if lst and lst.val < min_val:
                    min_val = lst.val
                    min_index = i
            if min_val is inf:
                break

            res.next = lists[min_index]
            res = res.next
            lists[min_index] = lists[min_index].next

        return original_pointer.next






