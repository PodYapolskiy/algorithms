from queue import PriorityQueue
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        """
        Time:  O(n log n)
        Space: O(n)
        """
        graph = defaultdict(PriorityQueue)

        # lexically sorted priority queue of departures destinations
        for departure, arrival in tickets:
            graph[departure].put(arrival)

        itinerary = []
        stack = ["JFK"]
        while stack:
            if not graph[stack[-1]].empty():
                stack.append(graph[stack[-1]].get())
            else:  # when all arrivals of destinatinations are visited
                itinerary.append(stack.pop())

        return itinerary[::-1]  # due to stack nature
