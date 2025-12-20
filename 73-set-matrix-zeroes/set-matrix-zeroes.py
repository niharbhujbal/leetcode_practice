class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if matrix[row_ind][col_ind] == 0:
                    zero_rows.add(row_ind)
                    zero_cols.add(col_ind)
        
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if row_ind in zero_rows or col_ind in zero_cols:
                    matrix[row_ind][col_ind] = 0


            
                