class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


# here we go to middle element and check its right side neighbour
# if left neighbour is greater than middle element then there has to be a peak element in right side
# we don't care there might be or might not be a peak element in left side but we are sure that there is a peak in right side
# [1,2,3,1]
#      l
#      r
# mid = 2
