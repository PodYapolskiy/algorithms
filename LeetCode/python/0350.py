class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time:  O(n + m)
        Space: O(n + m)
        """
        d1, d2 = dict(), dict()

        for n in nums1:
            d1[n] = d1.get(n, 0) + 1

        for n in nums2:
            d2[n] = d2.get(n, 0) + 1

        result = []
        for key in list(set(d1.keys()).intersection(set(d2.keys()))):
            result.extend([key] * min(d1[key], d2[key]))

        return result
