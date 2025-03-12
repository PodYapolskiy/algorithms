from collections import deque


def main():
    """
    Time:  O(n log n)
    Space: O(n^2)
    """
    n, m = list(map(int, input().split()))
    graph = {}
    for _ in range(m):
        n1, n2 = list(map(int, input().split()))
        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()

        graph[n1].add(n2)
        graph[n2].add(n1)

    # nodes that are in graph but has no connections
    for n in range(1, n + 1):
        if n not in graph:
            graph[n] = set()

    visited = set()
    to_visit = deque([1])  # to effieciently pop from left and append to right for O(1)
    while len(to_visit) > 0:
        node = to_visit.popleft()  # pick next node to visit
        if node not in visited:
            visited.add(node)
            connections = list(graph[node])
            to_visit.extend(connections)  # pick next nodes to visit

    print(len(visited))
    visited = sorted(list(visited))
    print(" ".join(list(map(str, visited))))


if __name__ == "__main__":
    main()
