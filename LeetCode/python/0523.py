class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        mem = {0: -1}
        prefix_sum = 0

        for i, n in enumerate(nums):
            prefix_sum = (prefix_sum + n) % k

            if prefix_sum in mem:
                if i - mem[prefix_sum] > 1:  # ensure min len 2
                    return True
            else:  # update ONLY if module is not yet present
                mem[prefix_sum] = i

        return False
