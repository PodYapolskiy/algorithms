from rich import print


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        output = []

        right_bound, down_bound, left_bound, up_bound = n - 1, m - 1, 0, 0
        while len(output) < m * n:  # terminal condition (all elemenets are added)
            # moving from left to right
            row, col = up_bound, left_bound
            while col <= right_bound and len(output) < m * n:
                output.append(matrix[row][col])
                col += 1
            up_bound += 1  # move upper border on 1 next

            # moving from up to down
            row, col = up_bound, right_bound
            while row <= down_bound and len(output) < m * n:
                output.append(matrix[row][col])
                row += 1
            right_bound -= 1

            # moving from right to left
            row, col = down_bound, right_bound
            while col >= left_bound and len(output) < m * n:
                output.append(matrix[row][col])
                col -= 1
            down_bound -= 1

            # moving from down to up
            row, col = down_bound, left_bound
            while row >= up_bound and len(output) < m * n:
                output.append(matrix[row][col])
                row -= 1
            left_bound += 1

        return output


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = Solution().spiralOrder(matrix)
answer = [1, 2, 3, 6, 9, 8, 7, 4, 5]
if output != answer:
    print(f"{output} should be {answer}")

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output = Solution().spiralOrder(matrix)
answer = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
if output != answer:
    print(f"{output} should be {answer}")
