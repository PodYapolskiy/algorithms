from string import ascii_uppercase


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time:  O(26n) = O(n)
        Space: O(1)
        """
        max_len = 0
        for letter in ascii_uppercase:
            start = counter = 0

            for i, l in enumerate(s):
                counter += 1 if l == letter else 0

                while i - start + 1 - counter > k:
                    if s[start] == letter:
                        counter -= 1
                    start += 1

                max_len = max(max_len, i - start + 1)

        return max_len

    def characterReplacementSolution(self, s: str, k: int) -> int:
        """
        Time:  O(n)
        Space: O(26) = O(1)
        """
        max_len = left = 0
        freq = {}

        for right, letter in enumerate(s):
            freq[letter] = freq.get(letter, 0) + 1
            max_len = max(max_len, freq[letter])

            if right - left + 1 - max_len > k:
                freq[s[left]] -= 1
                left += 1

        return len(s) - left
