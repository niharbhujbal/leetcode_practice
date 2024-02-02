class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        for ro_no, row in enumerate(matrix):
            for col_no, val in enumerate(matrix[ro_no]):
                if ro_no - 1 < 0 or col_no - 1 < 0:
                    continue
                elif matrix[ro_no - 1][col_no - 1] != val:
                    return False
        return True


# Iterate over all the element and just check upper diagonal element is not same
# def check_diag(r,c,val):
#     if r >= len(matrix) or c >= len(matrix[0]):
#         return 1
#     if matrix[r][c] != val:
#         return 0
#     # move to next diagonal element
#     return check_diag(r+1,c+1,val)

# # vertical loop
# vertical = 0
# for r in range(len(matrix)):
#     vertical += check_diag(r,0,matrix[r][0])
# if vertical != len(matrix):
#     return False
# horizontal = 0
# for c in range(1,len(matrix[0])):
#     horizontal += check_diag(0,c,matrix[0][c])
# if horizontal != len(matrix[0])-1:
#     return False
# return True
# one function which check digonal elements when given an element and equivalent value to check
# terminating conditoin is r > len or c > len return 1
# element not equal then return 0
# call same function with r+1 c+1
# now two loop which call all the column and row elements with this function
