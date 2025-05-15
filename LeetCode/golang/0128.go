func longestConsecutive(nums []int) int {
	/**
	* Time:  O(n)
	* Space: O(n)
	*/
	mem := make(map[int]struct{})  // empty struct is a value (no overhead)
    for _, num := range nums {
        mem[num] = struct{}{}
    }

    maxLength := 0
    for num, _ := range mem {
        if _, exists := mem[num - 1]; !exists { // check if not in the beginning of sequence
            length := 0
            
            for { // while has neighbors to right
                if _, exists := mem[num + length]; !exists {
                    break
                }
                length++
            }

            maxLength = max(maxLength, length)
        }
    }

    return maxLength
}
