# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n

        while start <= end:
            num = start + (end - start) // 2
            if guess(num) == 0:
                return num
            elif guess(num) == 1:
                start = num + 1
            else:
                end = num - 1

        return 0
