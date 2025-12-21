class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = [[0]*i for i in range(1,numRows+1)]
        
        # terminating condition
        for r, row in enumerate(matrix):
            for c, ele in enumerate(row):
                if c == 0 or r == c:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = matrix[r-1][c] + matrix[r-1][c-1]
        return matrix