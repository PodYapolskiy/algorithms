class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Time:  O(log n)
        Space: O(1)
        """
        if nums[0] <= nums[-1]:  # sorted on % len(nums) == 0
            return nums[0]  # in case len(nums) == 1 also works

        minima = float("inf")
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            minima = min(minima, nums[mid])
            if nums[mid] >= nums[end]:  # step in the wrong sorted part
                start = mid + 1
            else:  # step as left as possible in the correctly sorted part
                end = mid - 1

        return minima
