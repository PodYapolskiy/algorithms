class Solution:
    def isPalindrome(self, s, start, end) -> tuple[int, int]:
        while start < end and s[start] == s[end]:
            start += 1
            end -= 1
        return start, end

    def validPalindrome(self, s: str) -> bool:
        start, end = self.isPalindrome(s, 0, len(s) - 1)

        if start >= end:  # palindrom from beginning
            return True  # true if indexes at least overlap (odd) or i > j (even)

        # check solution abc(X)...cba where check for "..." substring
        right_shift_start, right_shift_end = self.isPalindrome(s, start + 1, end)
        # check solution abcX..(.)cba where check for "X.." substring
        left_shift_start, left_shift_end = self.isPalindrome(s, start, end - 1)

        return (
            right_shift_start >= right_shift_end or left_shift_start >= left_shift_end
        )
