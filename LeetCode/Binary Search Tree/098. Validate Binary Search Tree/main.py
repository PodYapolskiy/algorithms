from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], down_bound=None, up_bound=None
    ) -> bool:
        # definetely can say that invalid
        if (up_bound is not None and root.val >= up_bound) or (
            down_bound is not None and root.val <= down_bound
        ):
            return False

        # if node is terminal
        if root.left is None and root.right is None:
            return True

        # recursion in action, key moment is bounds values
        left = self.isValidBST(root.left, down_bound, root.val) if root.left else True
        right = self.isValidBST(root.right, root.val, up_bound) if root.right else True

        return left and right
