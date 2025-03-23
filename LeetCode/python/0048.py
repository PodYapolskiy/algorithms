class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transpose
        for row in range(n - 1):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # mirror
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = (
                    matrix[row][n - col - 1],
                    matrix[row][col],
                )
