class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_space = s.rfind(" ")
        return len(s) - last_space - 1 if last_space != -1 else len(s)
