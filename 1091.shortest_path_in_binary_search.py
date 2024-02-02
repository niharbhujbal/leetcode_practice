from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = []

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        q = deque()
        # (r,c,visited,length_of_path)
        q.append((0, 0, 0))
        visited = set()
        while len(q) != 0:
            r, c, length_of_path = q.popleft()

            if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
                ans.append(length_of_path + 1)
                continue
            elif (
                r > len(grid) - 1
                or c > len(grid[0]) - 1
                or r < 0
                or c < 0
                or (r, c) in visited
            ):
                continue
            elif grid[r][c] != 0:
                continue
            visited.add((r, c))
            length_of_path += 1
            for path in directions:
                q.append((r + path[0], c + path[1], length_of_path))

        if len(ans) == 0:
            return -1
        else:
            return min(ans)


# dfs for this problem fails since it will take a lot of time to process the solution
# we have to do bfs for this problem first we will lay out all the direction a node can go
# we will create a queue in which we will upload all the directions with visited node and length o the path takes with r,c
