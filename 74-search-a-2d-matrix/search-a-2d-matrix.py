class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # find the array to search in the matrix
        left = 0
        right = m - 1
        row = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            # check if the element is inside
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if row == float('inf'):
            return False
        
        left = 0
        right = n-1
        
        while left <= right:
            mid  = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

        

