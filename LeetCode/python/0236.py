from rich import print


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def argmin(arr: list[int]):
        return min(range(len(arr)), key=lambda x: arr[x])

    def dfs(self, node: TreeNode, depth: int = 0):
        self.trace.append(node.val)
        self.depths.append(depth)

        if node not in self.visited and (
            # we are able not to continue search if p and q are already visited (we know depths and trace)
            self.p not in self.visited
            or self.q not in self.visited
        ):
            self.visited.add(node)
            self.nodes[node.val] = node

            if node.left:
                self.dfs(node.left, depth + 1)

                # add current node after quiting left subtree
                self.trace.append(node.val)
                self.depths.append(depth)

            if node.right:
                self.dfs(node.right, depth + 1)

                # add currect after quiting right subtree
                self.trace.append(node.val)
                self.depths.append(depth)

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.p, self.q = p, q
        self.visited = set()
        self.nodes: dict[int, TreeNode] = {}  # mapping val -> node
        self.trace, self.depths = [], []

        # collect trace (euler path), depths, nodes and visited inside
        self.dfs(root, 0)

        # first occuerence of both p and q nodes
        p_index, q_index = self.trace.index(p.val), self.trace.index(q.val)

        # reduce our LCA(p, q) to RMQ(start, end)
        start, end = min(p_index, q_index), max(p_index, q_index)

        # find index of LCA by taking start index + index of minimum depth
        lca_node_ind = start + self.argmin(self.depths[start : end + 1])
        lca_node_val = self.trace[lca_node_ind]

        return self.nodes.get(lca_node_val, root)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(Solution().lowestCommonAncestor(root, root.left, root.right).val == 3)
print(Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val == 5)
