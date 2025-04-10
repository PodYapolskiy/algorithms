class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        info = {  # letter: (precedence, value)
            "M": (6, 1000),
            "D": (5, 500),
            "C": (4, 100),
            "L": (3, 50),
            "X": (2, 10),
            "V": (1, 5),
            "I": (0, 1),
        }

        integer = 0
        last = "I"
        for i in range(len(s)):
            letter = s[~i]  # i-th index from the end

            # update the highest precedence term on the cur moment
            if info[letter][0] > info[last][0]:
                last = letter

            # if cur letter is equal to the one with higher precende on cur step, add, otherwise subtract
            sign = 1 if letter == last else -1
            integer += sign * info[letter][1]

        return integer
