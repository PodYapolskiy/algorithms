class Node:
    def __init__(self, val=None):
        self.prev = None
        self.next = None
        self.val = val


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        mem = {}
        for num in nums:
            if num not in mem:
                mem[num] = Node(num)

                left_num, right_num = num - 1, num + 1
                if left_num in mem:
                    mem[left_num].next = mem[num]
                    mem[num].prev = mem[left_num]
                if right_num in mem:
                    mem[right_num].prev = mem[num]
                    mem[num].next = mem[right_num]

        max_counter = 0
        for node in list(mem.values()):
            if node.prev is None:
                counter = 0
                ptr = node
                while ptr:
                    counter += 1
                    ptr = ptr.next
                max_counter = max(max_counter, counter)

        return max_counter
