class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Time:  O(n)
        Space: O(k)
        """
        seen: set[int] = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if i >= k:
                seen.remove(nums[i - k])

        return False
