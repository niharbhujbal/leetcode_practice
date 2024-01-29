class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # for i in matrix:
        #     index = bisect.bisect_left(i,target)
        #     if index == len(i) or i[index] != target:
        #         continue
        #     else:
        #         return True
        # else:
        #     return False
        m = self.matrix_binary_search(0, len(matrix), matrix, target)
        n = self.binary_search(0, len(matrix[m]), matrix[m], target)
        return n != -1

    def matrix_binary_search(self, start, end, matrix, target):
        mid = (start + end) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return mid
        elif end - start <= 1:
            return -1
        elif matrix[mid][-1] < target:
            return self.matrix_binary_search(mid, end, matrix, target)
        elif matrix[mid][0] > target:
            return self.matrix_binary_search(start, mid, matrix, target)

    def binary_search(self, start, end, array, target):
        mid = (start + end) / 2
        mid = int(mid)
        if array[mid] == target:
            return mid
        elif start == mid:
            return -1
        elif target < array[mid]:
            return self.binary_search(start, mid, array, target)
        else:
            return self.binary_search(mid, end, array, target)


# we will do double binary search
# first one is to find in which array of matrix we should do binary search and second is to the normal binary search
# for matrix binary search function will take start, eend index vertically of a matrx and target
# we will calculate vertical mid. look at the first and last value of the row
# if our target is in the rage the return the mid
# else check if difference between end and start is one if so check if target exist in end ends index matrix if it dosen't then return -1
