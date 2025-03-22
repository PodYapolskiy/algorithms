class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        counter, n = 0, len(height)
        left = [height[0]] + [0] * (n - 1)
        right = [0] * (n - 1) + [height[n - 1]]

        # accumulate max left and max right for each index
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])
            right[n - i - 1] = max(height[n - i - 1], right[n - i])

        # find lowest height from left and right for each point and use it to calculate water
        for i in range(n):
            lowest = min(left[i], right[i])

            # if for the point height is lower than lowest border, increase counter
            if height[i] < lowest:
                counter += lowest - height[i]

        return counter


assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
