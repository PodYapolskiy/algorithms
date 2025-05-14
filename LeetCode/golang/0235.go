type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	/**
	* Time:  O(h)
	* Space: O(1)
	*/
	for { // while true
        if max(p.Val, q.Val) < root.Val {
            root = root.Left
        } else if min(p.Val, q.Val) > root.Val {
            root = root.Right
        } else {
            return root
        }
    }
}