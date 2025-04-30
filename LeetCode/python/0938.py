class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """

        def dfs(node) -> int:
            if not node:
                return 0

            if low <= node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            if low < node.val:
                return dfs(node.left)
            if node.val < high:
                return dfs(node.right)

        return dfs(root)
