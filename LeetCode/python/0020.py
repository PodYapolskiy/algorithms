class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time:  O(n)
        Space: O(n)
        """
        if len(s) % 2:
            return False

        braces = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for brace in s:
            if brace in braces:
                stack.append(brace)
            else:
                if not stack or braces[stack.pop()] != brace:
                    return False

        return not stack
