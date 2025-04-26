class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Time:  O(log n)
        Space: O(1)
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return -1
