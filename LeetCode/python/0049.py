class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Time:  O(n*k)
        Space: O(n*k)
        """
        d = {}
        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - 97] += 1  # get index [0, 26]

            key = tuple(key)  # each key is couner of letter as tuple
            d[key] = d.get(key, []) + [s]

        return list(d.values())
