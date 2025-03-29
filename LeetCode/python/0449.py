from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Encodes a tree to a single string.
        Time:  O(n)
        Space: O(n)
        """
        nodes = []

        def preorder(node: TreeNode | None) -> None:
            """DFS traversal"""
            if node:
                nodes.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        return " ".join(map(str, nodes))

    def deserialize(self, data: str) -> TreeNode | None:
        """Decodes your encoded data to tree.
        Time:  O(n)
        Space: O(n)
        """
        queue = deque(int(val) for val in data.split(" ") if val != "")

        def build(min_val: float, max_val: float) -> TreeNode | None:
            if queue and min_val < queue[0] < max_val:
                val = queue.popleft()

                node = TreeNode(val)
                node.left = build(min_val, val)
                node.right = build(val, max_val)

                return node

        return build(float("-inf"), float("inf"))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
