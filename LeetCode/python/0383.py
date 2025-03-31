from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)

        for k, v in a.items():
            if v > b.get(k, 0):
                return False

        return True
