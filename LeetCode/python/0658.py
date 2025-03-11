import heapq


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """
        Time:  O(n + k log k)
        Space: O(k)
        """
        if x <= arr[0]:  # base case when x is smaller than smallest element
            return arr[:k]  # take just first k elements
        if x >= arr[-1]:  # similar but from opposite side
            return arr[-k:]  # take k last elements

        # binary search due to sorted nature of array
        start, end = 0, len(arr) - 1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > x:
                end = mid - 1
            elif arr[mid] < x:
                start = mid + 1
            else:
                break  # when arr[mid] == x

        heap = []  # heap to keep k smallest elements
        middle = start + (end - start) // 2  # middle that we would use as start point
        if start < end:
            heapq.heappush(heap, arr[middle])  # add element that is exactly x
            k -= 1  # use k as counter of hom many left to find
            i, j = middle - 1, middle + 1  # pointers of prev and next elements
        else:  # if x does not exist in arr
            # depending on whether arr[middle] finally turn to be greater or lower choose i and j in order to find closest from both sides
            if arr[middle] > x:
                i, j = middle - 1, middle
            else:
                i, j = middle, middle + 1

        while k > 0:
            # if there are no elements on the left side, peak just all the right
            if i < 0:  # if ran out of smaller than x, peak only greater
                heapq.heappush(heap, arr[j])
                j += 1
            elif j >= len(arr):  # oppposite peak all smaller and closer to middle
                heapq.heappush(heap, arr[i])
                i -= 1
            else:  # when there is a choise which side to peak next
                left = abs(arr[i] - x)  # distance from x from left
                right = abs(arr[j] - x)  # similar to the right
                if left <= right:  # smaller elem when distance is smaller or equal
                    heapq.heappush(heap, arr[i])
                    i -= 1
                else:
                    heapq.heappush(heap, arr[j])
                    j += 1
            k -= 1  # we definetely peak strictly one smallest and closest element

        # peak k smallest elements from the heap
        return [heapq.heappop(heap) for _ in range(len(heap))]


assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
assert Solution().findClosestElements([1, 2, 4, 5, 6], 3, 3) == [1, 2, 4]
assert Solution().findClosestElements([1, 2, 4, 5, 6], 4, 3) == [1, 2, 4, 5]
assert Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
