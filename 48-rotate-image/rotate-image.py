class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row becomes col and col is n-1 -row
        n = len(matrix)
        rotated_indexs = set()
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if (row_ind,col_ind) not in rotated_indexs:
                    first = ele
                    second = matrix[col_ind][n-1-row_ind]
                    matrix[col_ind][n-1-row_ind] = first
                    rotated_indexs.add((col_ind,n-1-row_ind))

                    third = matrix[n-1-row_ind][n-1-col_ind]
                    matrix[n-1-row_ind][n-1-col_ind] = second
                    rotated_indexs.add((n-1-row_ind,n-1-col_ind))

                    fourth = matrix[n-1-col_ind][row_ind]
                    matrix[n-1-col_ind][row_ind] = third
                    rotated_indexs.add((n-1-col_ind,row_ind))

                    matrix[row_ind][col_ind] = fourth
                    rotated_indexs.add((row_ind,col_ind))
            

