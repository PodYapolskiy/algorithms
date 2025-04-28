class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time:  O(log(n*m))
        Space: O(1)
        """
        n, m = len(matrix), len(matrix[0])
        start_row, end_row = 0, n - 1

        while start_row <= end_row:
            row = start_row + (end_row - start_row) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:  # is only possible row
                start_col, end_col = 0, m - 1

                while start_col <= end_col:
                    col = start_col + (end_col - start_col) // 2

                    if matrix[row][col] == target:
                        return True
                    elif matrix[row][col] > target:
                        end_col = col - 1
                    elif matrix[row][col] < target:
                        start_col = col + 1

                return False
            elif matrix[row][0] > target:
                end_row = row - 1
            elif matrix[row][-1] < target:
                start_row = row + 1

        return False
