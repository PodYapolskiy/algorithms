class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Time:  O(n^2)
        Space: O(n)
        """
        n = len(board)
        rows, cols, cells = (
            {row: set() for row in range(n)},
            {col: set() for col in range(n)},
            {cell: set() for cell in range(n)},
        )

        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if num == ".":
                    continue

                cell = 3 * (row // 3) + col // 3
                if num in rows[row] or num in cols[col] or num in cells[cell]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                cells[cell].add(num)

        return True
