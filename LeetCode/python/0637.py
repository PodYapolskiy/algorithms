from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        """
        Time:  O(n)
        Space: O(n)
        """
        if not root:
            return []

        cur_h = h = 0
        cur_sum = cur_cnt = 0

        answer = []
        queue = deque([(root, h)])
        while queue:
            node, h = queue.popleft()

            # on new level, append previous level's result
            if h != cur_h:
                cur_h += 1
                cur_sum = cur_cnt = 0
                answer.append(cur_sum / cur_cnt)

            # handling Nones and update cur layer's stats
            if node:
                cur_sum += node.val
                cur_cnt += 1

                # BFS located here
                queue.append((node.left, h + 1))
                queue.append((node.right, h + 1))

        return answer
