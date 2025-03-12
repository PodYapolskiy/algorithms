class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time:  O(n^2)
        Space: O(n^2)
        """
        n = len(s)
        mem = [[False] * n for _ in range(n)]
        ans_i, ans_j = 0, 0

        # single chars are always palindroms
        for i in range(n):
            mem[i][i] = True

        # 2 adjacent chars always should be checked for based cases
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                mem[i][i + 1] = True
                ans_i, ans_j = i, i + 1

        # differences between start and end
        for diff in range(2, n):
            for start in range(n - diff):
                end = start + diff

                # if start and end chars are equal and substring between them is palindrom
                if s[start] == s[end] and mem[start + 1][end - 1]:
                    mem[start][end] = True
                    ans_i, ans_j = start, end

        return s[ans_i : ans_j + 1]
