class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time:  O(n^2)
        Space: O(n)
        """
        nums.sort()  # O(n log n)
        answer = []
        n = len(nums)

        for fixed in range(n - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            start, end = fixed + 1, n - 1
            while start < end:
                total = nums[fixed] + nums[start] + nums[end]
                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    answer.append([nums[fixed], nums[start], nums[end]])
                    start += 1

                    # move start in order not to make duplicates
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        return answer
