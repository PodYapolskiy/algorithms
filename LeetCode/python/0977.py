class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Time:  O(n)
        Space: O(n)
        """
        if nums[0] >= 0:  # inplace when no negatives
            for i in range(len(nums)):
                nums[i] = nums[i] ** 2
            return nums

        if nums[-1] <= 0:  # inpalce when no positives
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = nums[i] ** 2
            nums = nums[::-1]
            return nums

        result = []
        i, j = 0, len(nums) - 1
        while i <= j:  # 2 pointers strategy to new array
            left = nums[i] ** 2
            right = nums[j] ** 2
            if left <= right:
                result.append(right)
                j -= 1
            else:
                result.append(left)
                i += 1

        return result[::-1]
