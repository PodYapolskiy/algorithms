class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        visited = set()

        # set of all nodes from A chain
        while headA is not None:
            visited.add(headA)
            headA = headA.next

        # check if any node from B chain is in visited (means intersection)
        while headB is not None:
            if headB in visited:
                return headB
            headB = headB.next

        return None
