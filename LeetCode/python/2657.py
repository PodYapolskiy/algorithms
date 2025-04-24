from collections import defaultdict


class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """
        Time:  O(n)
        Space: O(n)
        """
        mem = defaultdict(int)
        pca = []
        cnt = 0

        for i in range(len(A)):
            mem[A[i]] += 1
            mem[B[i]] += 1

            if A[i] == B[i] and mem[A[i]] == 2:  # handle when both immidately
                cnt += 1
            else:
                if mem[A[i]] == 2:
                    cnt += 1
                if mem[B[i]] == 2:
                    cnt += 1

            pca.append(cnt)

        return pca
