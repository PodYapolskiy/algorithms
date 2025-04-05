class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        area, start, end = 0, 0, len(height) - 1

        while start < end:
            area = max(area, min(height[start], height[end]) * (end - start))

            # shift the lowest edge
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area
