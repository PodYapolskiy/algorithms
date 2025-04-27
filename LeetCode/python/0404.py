class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        """
        Time:  O(n) - each node
        Space: O(n) | O(h) in balanced case (height of the tree)
        """

        def dfs(node: TreeNode | None, is_left: bool):
            if not node:
                return 0
            if not node.left and not node.right:  # leaf
                return node.val if is_left else 0  # main "if" comes from argument
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
