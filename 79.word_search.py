class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r >= len(board)
                or c >= len(board[0])
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))
            res = (
                dfs(r, c + 1, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r - 1, c, i + 1)
            )
            path.remove((r, c))

            return res

        for row_no, row in enumerate(board):
            for col_no, ele in enumerate(row):
                if dfs(row_no, col_no, 0):
                    return True
        return False
