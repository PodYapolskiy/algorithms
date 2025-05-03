class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time:  O(n)
        Space: O(n)
        """
        return " ".join([word for word in s.strip().split(" ") if word][::-1])
