from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Time:  O(n)
        Space: O(n)
        """
        cur_map, p_map = {}, Counter(p)
        indexes = []
        for i in range(len(s)):
            cur_map[s[i]] = cur_map.get(s[i], 0) + 1

            if i >= len(p):
                cur_map[s[i - len(p)]] -= 1
                if cur_map[s[i - len(p)]] == 0:
                    del cur_map[s[i - len(p)]]

            if cur_map == p_map:  # O(num of vocab, here is fixed 26)
                indexes.append(i - len(p) + 1)

        return indexes
