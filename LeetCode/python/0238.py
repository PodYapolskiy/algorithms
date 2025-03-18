# Input: nums = [1, 2, 3, 4]
# l -> r [1, 2, 6, 24]
# l <- r [24, 24, 12, 4]
# Output: [24, 12, 8, 6]

# Input: nums = [-1, 1, 0, -3, 3]
# l -> r [-1, -1, 0, 0, 0]
# l <- r [0, 0, 0, -9, 3]
# Output: [0, 0, 9, 0, 0]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Time:  O(n)
        Space: O(1)
        """
        result = [1] * len(nums)
        prev, post, n = 1, 1, len(nums)

        for i in range(n):
            result[i] *= prev
            prev *= nums[i]

        for i in range(n - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result
