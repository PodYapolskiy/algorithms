import "math"

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func isValidSubtree(node *TreeNode, low int, up int) bool {
    if node == nil {
        return true
    }
    if node.Val <= low || node.Val >= up {
        return false
    }
    return isValidSubtree(node.Left, low, node.Val) && isValidSubtree(node.Right, node.Val, up)
}

func isValidBST(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return isValidSubtree(root.Left, math.MinInt64, root.Val) && isValidSubtree(root.Right, root.Val, math.MaxInt64)
}