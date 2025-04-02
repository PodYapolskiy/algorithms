class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Time:  O(log n)
        Space: O(1)
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (end - start) // 2 + start

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start
