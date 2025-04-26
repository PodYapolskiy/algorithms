class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        prefix, min_prefix, max_sum = 0, 0, float("-inf")

        for num in nums:
            prefix += num

            max_sum = max(max_sum, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return max_sum
