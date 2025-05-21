func longestOnes(nums []int, k int) int {
	maxLen, start, end, zeros := 0, 0, 0, 0

	for end < len(nums) {
		if nums[end] == 0 {
			zeros++
		}

		for zeros > k {
			if nums[start] == 0 {
				zeros--
			}
			start++
		}

		maxLen = max(maxLen, end - start + 1)
		end++
	}

	return maxLen
}