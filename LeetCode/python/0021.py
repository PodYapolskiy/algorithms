class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """
        Time:  O(n + m)
        Space: O(1)
        """
        if not list1:
            return list2
        if not list2:
            return list1

        root = ListNode()
        temp = root
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next

        while list1:
            temp.next = list1
            temp = temp.next
            list1 = list1.next

        while list2:
            temp.next = list2
            temp = temp.next
            list2 = list2.next

        return root.next
