from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    queue = deque()
                    queue.append((r,c))
                    grid[r][c] = "0"

                    while queue:
                        nr, nc = queue.popleft()
                        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nnr, nnc = nr+dr, nc + dc
                            if 0 <= nnr < m and 0 <= nnc < n and grid[nnr][nnc] == "1":
                                grid[nnr][nnc] = "0"
                                queue.append((nnr, nnc))
        
        return islands
