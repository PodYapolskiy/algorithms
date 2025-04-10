class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Time:  O(n * k)
        Space: O(1)
        """
        min_length = float("inf")
        for s in strs:
            min_length = min(min_length, len(s))

        for i in range(min_length):
            letter = strs[0][i]
            for s in strs[1:]:
                if s[i] != letter:
                    return s[:i]

        return strs[0][:min_length]
