class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if matrix[row_ind][col_ind] == 0:
                    zeros.append((row_ind,col_ind))
        
        for row_ind, col_ind in zeros:
            # up
            zr = row_ind
            zc = col_ind
            while zr >=0:
                matrix[zr][zc] = 0
                zr -= 1
            
            # down
            zr = row_ind
            zc = col_ind
            while zr < m:
                matrix[zr][zc] = 0
                zr += 1

            # left
            zr = row_ind
            zc = col_ind
            while zc >= 0:
                matrix[zr][zc] = 0
                zc -= 1
            # right
            zr = row_ind
            zc = col_ind
            while zc < n:
                matrix[zr][zc] = 0
                zc += 1

            
                