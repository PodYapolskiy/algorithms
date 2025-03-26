class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]

        count = i = j = 0
        up_bound = left_bound = 0
        right_bound = down_bound = n - 1
        while count < n**2:
            # right
            while count < n**2 and j <= right_bound:
                matrix[i][j] = count + 1
                count += 1
                j += 1
            j -= 1
            i += 1
            up_bound += 1

            # down
            while count < n**2 and i <= down_bound:
                matrix[i][j] = count + 1
                count += 1
                i += 1
            i -= 1
            j -= 1
            right_bound -= 1

            # left
            while count < n**2 and j >= left_bound:
                matrix[i][j] = count + 1
                count += 1
                j -= 1
            j += 1
            i -= 1
            down_bound -= 1

            # up
            while count < n**2 and i >= up_bound:
                matrix[i][j] = count + 1
                count += 1
                i -= 1
            i += 1
            j += 1
            left_bound += 1

        return matrix


assert Solution().generateMatrix(1) == [[1]]
assert Solution().generateMatrix(2) == [[1, 2], [4, 3]]
assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert Solution().generateMatrix(4) == [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]
