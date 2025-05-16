from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Time:  O(n)
        Space: O(n)
        """
        if not root:
            return []

        # bfs
        traversal = []
        queue = deque([(root, 0)])
        while queue:
            node, h = queue.popleft()

            if len(traversal) == h:
                traversal.append([])

            traversal[h].append(node.val)

            if node.left:
                queue.append((node.left, h + 1))
            if node.right:
                queue.append((node.right, h + 1))

        def reverse(arr: list[int]):
            i, j = 0, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        # reverse all odd levels in tree
        for level in range(len(traversal)):
            if level % 2 == 1:
                reverse(traversal[level])

        return traversal
