class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        summary, left, min_len = 0, 0, float("inf")

        for right in range(len(nums)):
            summary += nums[right]

            while summary >= target:
                min_len = min(min_len, right - left + 1)
                summary -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0


assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
