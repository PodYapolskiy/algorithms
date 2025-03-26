class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Time:  O(log(min(m, n)))
        Space: O(1)
        """
        if len(nums1) > len(nums2):  # nums1 should be smaller
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            # A
            maxLeftA = nums1[partitionA - 1] if partitionA > 0 else float("-inf")
            minRightA = nums1[partitionA] if partitionA < m else float("inf")

            # B
            maxLeftB = nums2[partitionB - 1] if partitionB > 0 else float("-inf")
            minRightB = nums2[partitionB] if partitionB < n else float("inf")

            # main condition
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1


assert abs(Solution().findMedianSortedArrays([1, 3], [2]) - 2.0) < 1e-5
assert abs(Solution().findMedianSortedArrays([1, 2], [3, 4]) - 2.5) < 1e-5
