func Abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func findClosestElements(arr []int, k int, x int) []int {
	/**
	* Time:  O(n-k)
	* Space: O(1)
	*/
	start, end := 0, len(arr) - 1

	for end - start + 1 > k {
		if Abs(arr[start] - x) <= Abs(arr[end] - x) {
			end--
		} else {
			start++
		}
	}
	return arr[start:end+1]
}