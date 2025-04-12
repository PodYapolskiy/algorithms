class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        """
        Time:  O(min(n, m))
        Space: O(min(n, m))
        """
        first = second = 0

        intersections = []
        while first < len(firstList) and second < len(secondList):
            interval = [
                max(firstList[first][0], secondList[second][0]),
                min(firstList[first][1], secondList[second][1]),
            ]
            if interval[0] <= interval[1]:  # has intersection
                intersections.append(interval)

            # move depending on intervals' ends
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1

        return intersections
