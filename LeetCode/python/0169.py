class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        count = candidate = 0

        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1

        return candidate
