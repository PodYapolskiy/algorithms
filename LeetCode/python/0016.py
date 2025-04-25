class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        Time:  O(n^2)
        Space: O(1)
        """
        nums = sorted(nums)  # O(n log n)
        n = len(nums)
        closest_sum = float("inf")

        for fixed in range(n - 2):
            start, end = fixed + 1, n - 1
            while start < end:
                current_sum = nums[fixed] + nums[start] + nums[end]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum > target:
                    end -= 1
                elif current_sum < target:
                    start += 1
                else:
                    return target

        return closest_sum
