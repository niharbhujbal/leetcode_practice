class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(i,j):
            nonlocal m,n,grid
            if i>= m or i < 0 or j >= n or j < 0 or grid[i][j] == '0':
                return
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            grid[i][j] = '0'
            for l,k in directions:
                dfs(i+l, j+k)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
