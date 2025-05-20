func removeDuplicates(nums []int) int {
	/**
	* Time:  O(n)
	* Space: O(1)
	*/
	last := 1 // last valid
    curr := 1

    for curr < len(nums) {
        if curr < 2 || nums[last - 2] != nums[curr] {
            nums[last] = nums[curr]
            last++
        }

        curr++
    }

    return last
}