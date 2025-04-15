class Solution:
    def maxPower(self, s: str) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        count, power, last = 0, 0, None,
        for l in s:
            count = count + 1 if l == last else 1
            last = l
            power = max(power, count)
        return power
