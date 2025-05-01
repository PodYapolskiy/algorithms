class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Time:  O(n)
        Space: O(k), k << n
        """
        mem = {}  # O(26) = O(k)
        for idx, sym in enumerate(s):
            mem[sym] = [mem[sym][0], idx] if sym in mem else [idx, idx]

        # collect intervals and sort by beginning O(26 log 26) = O(1)
        intervals = sorted(mem.values(), key=lambda interval: interval[0])

        # iterate through partions, merge if needed
        partitions = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > partitions[-1][1]:  # new partition
                partitions.append(interval)
            elif interval[1] > partitions[-1][1]:  # extend current partition
                partitions[-1][1] = interval[1]

        return list(map(lambda interval: interval[1] - interval[0] + 1, partitions))
