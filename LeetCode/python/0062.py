from rich import print


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]


output = Solution().uniquePaths(3, 7)
if output != 28:
    print(f"{output} should equal to 28")

output = Solution().uniquePaths(3, 2)
if output != 3:
    print(f"{output} should equal to 3")
