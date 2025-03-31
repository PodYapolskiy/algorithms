from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Time:  O(n log k)
        Space: O(k)
        """
        pq = PriorityQueue()  # here pq needs 2nd argument for unique number

        # put first pointer of each linked list into pq
        for ll in lists:
            if ll:
                pq.put((ll.val, id(ll), ll))

        root = curr = ListNode()
        while not pq.empty():
            temp = pq.get()[2]  # temp is picked node pointer

            curr.next = temp  # current final sorted linked list node
            curr = curr.next  # move to the next position to sort

            if temp.next:  # insert next temp's node next into pq
                pq.put((temp.next.val, id(temp.next), temp.next))

        return root.next
