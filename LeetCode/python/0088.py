class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k, i, j = 0, m - 1, n - 1
        while k < m + n:
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[~k] = nums1[i]
                    i -= 1
                else:
                    nums1[~k] = nums2[j]
                    j -= 1
            elif j >= 0:  # if nums2 has left with all lower elems
                nums1[~k] = nums2[j]
                j -= 1
            else:  # if nums1 left with all lower elems
                nums1[~k] = nums1[i]
                i -= 1

            k += 1  # counter of placed correctly elems
