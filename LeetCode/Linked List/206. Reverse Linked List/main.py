from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if no or one element are present
        if head is None or head.next is None:
            return head

        # temporary variables (pointers) to control previous and next elements
        node, temp = None, head.next

        while head is not None:
            head.next = node  # reverse next for current node to prev
            node = head  # move prev to current
            head = temp  # move current to next
            temp = head.next if head is not None else None  # move next if possible

        return node
