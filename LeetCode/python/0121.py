class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        max_profit, min_price = 0, float("inf")

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
