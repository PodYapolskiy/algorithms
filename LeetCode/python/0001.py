class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mem = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mem:
                return [mem[diff], i]
            mem[nums[i]] = i
        return [-1, -1]
