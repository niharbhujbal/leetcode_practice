class Solution:
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited_master = set()
        visted_set = set()

        def dfs(r, c, visited):
            if (
                ((r, c) in visited)
                or ((r, c) in visted_set)
                or r >= m
                or c >= n
                or r < 0
                or c < 0
                or grid[r][c] != 1
                or (r, c) in visited_master
            ):
                return visited
            else:
                visited.add((r, c))
                visted_set.add((r, c))
                visited = dfs(r + 1, c, visited)
                visited = dfs(r, c + 1, visited)
                visited = dfs(r - 1, c, visited)
                visited = dfs(r, c - 1, visited)
                return visited

        max_i = 0
        for r in range(m):
            for c in range(n):
                ans = dfs(r, c, set())
                if len(ans) != 0:
                    max_i = max(max_i, len(ans))
                    visited_master.union(ans)

        return max_i
