from collections import deque


class RecentCounter:

    def __init__(self):
        self.pings = deque()

    def ping(self, t: int) -> int:
        """
        Time:  O(n)
        Space: O(1)
        """
        while self.pings and t - self.pings[0] > 3000:
            self.pings.popleft()
        self.pings.append(t)
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
