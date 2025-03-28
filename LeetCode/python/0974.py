class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        count = prefix_sum = 0
        mem = {0: 1}
        for n in nums:
            prefix_sum += n
            key = prefix_sum % k  # cur prefix modulo
            count += mem.get(key, 0)
            mem[key] = mem.get(key, 0) + 1  # update key occurences
        return count
