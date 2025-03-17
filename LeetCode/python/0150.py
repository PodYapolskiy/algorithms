class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        opers = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token in opers:
                b = stack.pop()
                a = stack.pop()
                stack.append(opers[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()
