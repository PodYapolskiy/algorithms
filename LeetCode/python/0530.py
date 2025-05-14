class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        arr = []

        def inorder(node):
            if not node:
                return

            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)

        min_dif = float("inf")
        for i in range(len(arr) - 1):
            min_dif = min(min_dif, arr[i + 1] - arr[i])

        return min_dif
