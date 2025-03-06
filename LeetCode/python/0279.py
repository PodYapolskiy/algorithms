class Solution:
    def numSquares(self, n: int) -> int:
        #
        dp = [0] + [float("inf")] * n

        # iterate until n
        for i in range(1, n + 1):
            # j is sqrt value of j-th perfect square
            j, min_val = 1, float("inf")

            # for each j-th perfect square until exceeds i-th number
            while j * j <= i:
                # take min of prev and accumulated stat of prev perfect square
                min_val = min(min_val, dp[i - j * j] + 1)
                dp[i] = min_val
                j += 1

        return dp[n]


assert Solution().numSquares(12) == 3
assert Solution().numSquares(13) == 2
