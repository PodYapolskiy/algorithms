class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, node: TreeNode | None, depth: int = 0) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        if not node:
            return depth

        left = self.depth(node.left, depth + 1)
        right = self.depth(node.right, depth + 1)

        # if any subtree is imbalanced or current node notices imbalance
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right)

    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.depth(root) != -1
