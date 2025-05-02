import heapq
import random
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time:  O(n log k)
        Space: O(n + k)
        """
        if k == len(nums):  # O(1)
            return nums

        counter = Counter(nums)  # O(n)
        return heapq.nlargest(k, counter.keys(), key=counter.get)  # O(n log k)

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        """
        Time:  O(n) [avg], O(n^2) [worst]
        Space: O(n)
        """
        counter = Counter(nums)
        unique = list(counter.keys())
        n = len(unique)
        k_smallest_index = n - k

        def partition(left: int, right: int, pivot: int) -> int:
            """Lomuto's partition Scheme
            Time:  O(n)
            Space: O(1)
            """
            pivot_freq = counter[unique[pivot]]

            # swap pivot with the righest
            unique[pivot], unique[right] = unique[right], unique[pivot]

            # move all less than pivot to the left
            index = left
            for i in range(left, right):
                if counter[unique[i]] < pivot_freq:
                    unique[index], unique[i] = unique[i], unique[index]
                    index += 1

            # swap pivot with last poiter stop to have all less to the left
            unique[right], unique[index] = unique[index], unique[right]
            return index

        def quickselect(left: int, right: int) -> None:
            """
            Time:  O(n)
            Space: O(1)
            """
            if left == right:  # base case to leave
                return

            pivot = random.randint(left, right)
            pivot = partition(left, right, pivot)

            # found pivot where all righter elements are exactly k top frequent
            if k_smallest_index == pivot:
                return
            elif k_smallest_index < pivot:  # not enough frequent elems are taken
                quickselect(left, pivot - 1)
            else:  # too many frequent elems are taken
                quickselect(pivot + 1, right)

        quickselect(0, n - 1)
        return unique[k_smallest_index:]
