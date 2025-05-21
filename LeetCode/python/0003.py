class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time:  O(n)
        Space: O(n)
        """
        if len(s) < 2:  # 0 or 1 length strings
            return len(s)

        start, end, max_longest = 0, 1, 1
        mem = set([s[start]])  # visited unique chars (already with first)
        while end < len(s):
            while s[end] in mem:  # until dublicate position is reached
                mem.remove(s[start])  # remove visited by shorten window
                start += 1
            mem.add(s[end])  # add here immediately visited char
            max_longest = max(max_longest, end - start + 1)
            end += 1

        return max_longest
