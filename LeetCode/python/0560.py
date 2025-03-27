class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        mem = {0: 1}  # should present to increase count
        count = prefix_sum = 0
        for n in nums:
            prefix_sum += n
            count += mem.get(prefix_sum - k, 0)
            mem[prefix_sum] = mem.get(prefix_sum, 0) + 1
        return count


assert Solution().subarraySum([1, 1, 1], 2) == 2
assert Solution().subarraySum([1, 2, 3], 3) == 2
assert Solution().subarraySum([1, 4, 1, 2, 5, 4], 7) == 2
assert Solution().subarraySum([], 0) == 0
assert Solution().subarraySum([0], 0) == 1
assert Solution().subarraySum([1, 4, 0, 0, 4, 1], 5) == 6
