type ListNode struct {
    Val int
    Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	/**
	* Time:  O(n + m)
	* Space: O(max(n, m))
	*/
	root := &ListNode{}
    ptr := root
    shift := false

    for l1 != nil || l2 != nil || shift {
        sum := 0
        if l1 != nil {
            sum += l1.Val
        }
        if l2 != nil {
            sum += l2.Val
        }
        if shift {
            sum += 1
        }

        shift = sum > 9
        ptr.Next = &ListNode{Val: sum % 10}
        ptr = ptr.Next

        if l1 != nil {
            l1 = l1.Next
        }
        if l2 != nil {
            l2 = l2.Next
        }
    }

    return root.Next
}