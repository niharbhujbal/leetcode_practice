class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited_master = []
        visted_set = set()

        def dfs(r, c, visited):
            if (
                (r, c) in visited
                or (r, c) in visted_set
                or r >= m
                or c >= n
                or r < 0
                or c < 0
            ):
                return visited
            elif grid[r][c] != "1":
                return visited
            else:
                visited.add((r, c))
                visted_set.add((r, c))
                visited = dfs(r + 1, c, visited)
                visited = dfs(r, c + 1, visited)
                visited = dfs(r - 1, c, visited)
                visited = dfs(r, c - 1, visited)
                return visited

        for r in range(m):
            for c in range(n):
                ans = dfs(r, c, set())
                if len(ans) != 0:
                    visited_master.append(ans)
        return len(visited_master)


# create a function which takes row, col and visited (r,c) set
# if the r,c is not is visited set then chek if its a islandand add it to a master set
# call same function on all neghoubs
