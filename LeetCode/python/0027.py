class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[~k] = nums[~k], nums[i]
                k += 1
        return len(nums) - k
