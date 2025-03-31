class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area, cols = 0, len(matrix[0])
        heights = [0] * (cols + 1)  # last 0 to calc until the last real

        for row in matrix:
            # update heights
            for i in range(len(row)):
                heights[i] = heights[i] + 1 if row[i] != 0 else 0

            # stack instead of comparing columns
            stack = []
            for i in range(len(heights)):
                #  pop until the current height is samller than the top of the stack
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
