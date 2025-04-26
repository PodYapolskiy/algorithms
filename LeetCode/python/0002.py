class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        """
        Time:  O(n + m)
        Space: O(max(n, m))
        """
        root = ListNode()
        ptr = root
        shift = False
        while l1 or l2:
            s = 0
            s += l1.val if l1 else 0
            s += l2.val if l2 else 0
            s += 1 if shift else 0

            shift = s > 9

            ptr.next = ListNode(s % 10)
            ptr = ptr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if shift:
            ptr.next = ListNode(1)

        return root.next
