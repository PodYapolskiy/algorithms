from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Time:  O(n * m)
        Space: O(n * m)
        """
        n, m = len(grid), len(grid[0])
        counter = 0
        visited = set()
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(n):
            for j in range(m):
                # "water" and already visited island is not interested
                if grid[i][j] == "0" or (i, j) in visited:
                    continue

                # perform dfs via queue based approach
                queue = deque([(i, j)])
                while queue:
                    pos = queue.popleft()
                    if pos not in visited:
                        visited.add(pos)

                        for move in moves:
                            # get new potential positions by 4adj rule
                            new_i, new_j = pos[0] + move[0], pos[1] + move[1]

                            # expand our dfs only if new position is ground within boundaries
                            if (
                                0 <= new_i < n
                                and 0 <= new_j < m
                                and grid[new_i][new_j] == "1"
                            ):
                                queue.append((new_i, new_j))

                # finish of dfs means that we fully cover current island
                counter += 1

        return counter
