class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        points_set = set()
        x_min, x_max = float("inf"), -float("inf")

        for x, y in points:
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            points_set.add((x, y))

        s = x_min + x_max  # diff from edge to center
        return all((s - x, y) in points_set for x, y in points)


assert Solution().isReflected([[1, 1], [-1, 1]])
assert not Solution().isReflected([[1, 1], [-1, -1]])
assert Solution().isReflected([[-1, 1], [1, 2], [3, 2], [5, 1]])
assert Solution().isReflected([[-1, 1], [1, 2], [3, 2], [5, 1], [5, 1]])  # dublicate
