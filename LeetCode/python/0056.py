class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:  # overlapping
                result[-1][1] = max(result[-1][1], interval[1])  # pick the farthest

        return result
