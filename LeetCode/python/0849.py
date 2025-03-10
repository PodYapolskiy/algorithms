class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        i = zeros_len = 0

        while seats[i] == 0:  # if starts with zero (pick most left seat)
            zeros_len += 1
            i += 1
        max_dist = zeros_len  # assign zero or more (if zeros at the beginning)

        while i < len(seats):
            zeros_len = 0

            while i < len(seats) and seats[i] == 0:  # iterate until occupied
                zeros_len += 1
                i += 1

            if zeros_len == 0:  # if occupied, just try further
                i += 1
                continue

            max_dist = max(max_dist, (zeros_len + 1) // 2)

        if zeros_len > 0:  # if ends with zero (pick the most right place)
            max_dist = max(max_dist, zeros_len)

        return max_dist


assert Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert Solution().maxDistToClosest([1, 0, 0, 0]) == 3
assert Solution().maxDistToClosest([0, 1]) == 1
assert Solution().maxDistToClosest([0, 0, 0, 0, 1]) == 4
