class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head or not head.next:  # None or [.] n = 1
            return None

        count = 0
        before_nth = p = head  # 2 pointers
        while p:
            count += 1  # use nodes amount to determine if head should be removed
            p = p.next

            if count > n + 1:  # n + 1 as node before nth
                before_nth = before_nth.next

        if count == n:  # if head should be removed
            head = head.next
        else:  # remove by pointing before nth to after next
            before_nth.next = before_nth.next.next

        return head
