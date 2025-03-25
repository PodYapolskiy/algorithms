class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Time:  O(n)
        Space: O(1)
        """
        interval = [0, 0]
        for i, n in enumerate(nums):
            # start of new is less than prev's end
            # and end of new is larger than end of prev
            if i <= interval[1] and i + n > interval[1]:
                interval[1] = i + n

        return interval[1] >= len(nums) - 1
