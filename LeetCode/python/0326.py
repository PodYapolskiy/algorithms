class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        j = 0
        while 3 ** j < n:
            j += 1
        return 3 ** j == n
