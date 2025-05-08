class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, node: TreeNode | None) -> int:
        """
        Time:  O(log n)
        Space: O(1)
        """
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def countNodes(self, root: TreeNode | None) -> int:
        """
        Time:  O((log n)^2)
        Space: O(log n)
        """
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)
