class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # handle case when even root is None
        if not root:
            return []

        # if it is terminal node return value of node as 1 element list (base case)
        if not root.left and not root.right:
            return [root.val]

        # inorder means left -> root -> right
        left = self.inorderTraversal(root.left) if root.left else []
        middle = [root.val]
        right = self.inorderTraversal(root.right) if root.right else []

        return left + middle + right
