class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        s = n * (n + 1) // 2
        for num in nums:
            s -= num
        return s
