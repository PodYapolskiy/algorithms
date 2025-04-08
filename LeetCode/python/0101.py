class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricSubtree(self, a: TreeNode | None, b: TreeNode | None) -> bool:
        if not a or not b:
            return a == b

        if a.val != b.val:
            return False

        return self.isSymmetricSubtree(a.left, b.right) and self.isSymmetricSubtree(
            a.right, b.left
        )

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isSymmetricSubtree(root.left, root.right)
