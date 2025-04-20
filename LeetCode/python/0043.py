class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        N = len(num1) + len(num2)
        answer = [0] * N

        for i1, d1 in enumerate(num1[::-1]):
            for i2, d2 in enumerate(num2[::-1]):
                num_zeros = i1 + i2

                carry = answer[num_zeros]
                multiplication = int(d1) * int(d2) + carry

                answer[num_zeros] = multiplication % 10
                answer[num_zeros + 1] += multiplication // 10

        if answer[-1] == 0:
            answer.pop()

        return "".join(str(d) for d in reversed(answer))
