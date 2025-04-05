class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        k, last = 0, None
        for i in range(len(nums)):
            if nums[i] != last:
                last = nums[i]
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return k
