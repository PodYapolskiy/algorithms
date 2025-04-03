class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p or not q:  # if any is None other also should be
            return p == q

        return (
            p.val == q.val  # both are nodes, so should have same values
            and self.isSameTree(p.left, q.left)  # divide and conquer left subtrees
            and self.isSameTree(p.right, q.right)  # same for right subtrees
        )
