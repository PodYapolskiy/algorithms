func singleNumber(nums []int) int {
    answer := 0
    for _, n := range nums {
        answer ^= n
    }
    return answer
}