class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        """
        Time:  O(n^2)
        Space: O(n^2)
        """
        mem = {}
        answer = set()

        def postorder(root) -> str:
            left = postorder(root.left) if root.left else ""
            right = postorder(root.right) if root.right else ""
            serialized = f"{root.val} {left} {right}"

            occurences = mem.get(serialized, 0)
            if occurences == 1:  # helps avoid 4 / root and root \ 4
                answer.add(root)
            mem[serialized] = occurences + 1
            return serialized

        postorder(root)
        return list(answer)
