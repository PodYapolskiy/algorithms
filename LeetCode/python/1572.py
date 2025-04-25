class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        dim, dsum = len(mat), 0
        for i in range(dim):
            dsum += mat[i][i] + mat[i][~i]
        return dsum - mat[dim // 2][dim // 2] if dim % 2 else dsum
