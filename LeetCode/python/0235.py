class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Time:  O(n)
        Space: O(n)
        """
        traversal, heights = [], []
        self.p_index = self.q_index = None

        def inorder(node: TreeNode | None, h: int):
            if not node:
                return

            if node.left:
                inorder(node.left, h + 1)

            if node == p:
                self.p_index = len(traversal)
            if node == q:
                # print("zdarovo")
                self.q_index = len(traversal)

            traversal.append(node)
            heights.append(h)

            if node.right:
                inorder(node.right, h + 1)

        inorder(root, 0)

        # assert p_index is not None and q_index is not None
        p_index = self.p_index
        q_index = self.q_index
        if p_index > q_index:
            p_index, q_index = q_index, p_index

        # argmin
        min_index = min(range(p_index, q_index + 1), key=lambda i: heights[i])

        return traversal[min_index]
