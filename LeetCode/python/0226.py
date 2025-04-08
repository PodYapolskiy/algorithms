class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root or (not root.left and not root.right):
            return root

        left = root.left
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)

        return root
