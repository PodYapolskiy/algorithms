import "math"

func maxSubArray(nums []int) int {
	/*
	Time:  O(n)
	Space: O(1)
	*/
    curr_sum, best_sum := 0, math.MinInt
    for _, num := range nums {
        curr_sum = max(num, curr_sum + num)
        best_sum = max(best_sum, curr_sum)
    }
    return best_sum
}