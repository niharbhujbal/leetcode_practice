class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c, visited):
            if r >= m or r < 0 or c >= n or c < 0:
                return False
            elif board[r][c] == "X" or (r, c) in visited:
                return True
            else:
                visited.add((r, c))
                ans = (
                    dfs(r + 1, c, visited)
                    and dfs(r - 1, c, visited)
                    and dfs(r, c + 1, visited)
                    and dfs(r, c - 1, visited)
                )
                if ans:
                    board[r][c] = "X"
                return ans

        for r in range(m):
            for c in range(n):
                dfs(r, c, set())
        return board
