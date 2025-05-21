class Solution:
    def generate(self, s: str, open: int, close: int):
        if len(s) == self.n * 2:
            if open == close:
                self.arr.append(s)
            return

        if open < self.n:
            self.generate(s + "(", open + 1, close)
        if open > close:
            self.generate(s + ")", open, close + 1)

    def generateParenthesis(self, n: int) -> list[str]:
        """
        Time:  O(2^n)
        Space: O(n)
        """
        self.n = n
        self.arr = []

        self.generate("", 0, 0)

        return self.arr
