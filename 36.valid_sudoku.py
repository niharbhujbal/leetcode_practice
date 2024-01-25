class Solution:
    def isValidSudoku(self, board):
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [[set() for _ in range(N // 3)] for _ in range(N // 3)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box

                if val in boxes[r // 3][c // 3]:
                    return False
                boxes[r // 3][c // 3].add(val)

        return True


# create  row list with n sets and column list with n sets
# we want add elements in these sets as we iterate over them and if we find duplicate then its not a valid sudoku
# we will also have to create a box
