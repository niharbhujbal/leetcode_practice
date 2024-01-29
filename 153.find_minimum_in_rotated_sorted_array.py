class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right - 1] < nums[right]:
                right -= 1
            else:
                return nums[right]
            if nums[left] > nums[right]:
                left += 1
            else:
                return nums[left]
        return nums[left]


# intiate two pointers
# left most element and right most element
# while true loop
# if left element is bigger then right element the the array has been rotated so we want to know how many times it has been rotated
# so we will keep incrementing the left pointer until left < right or left = right
# the return the left pointer element
# one the right pointer as well if the right - 1 element is smaller than right the the decrement the right
# if it is larger then directly return the right
# [4,5,6,7,0,1,2]
#      L
#          R

# With binary search
# left, right = 0, len(nums) - 1
# while nums[left] > nums[right]:
#     middle  = (left + right) // 2
#     if nums[middle] < nums[right]:
#         right = middle
#     else:
#         left = middle + 1
# return nums[left]
# here keep the loop running until we find the actual sorted sortion of the array
# our goal is to find sorted portion
# so when we compare the middle with right if that is smaller that means middle is in sorted position so we should search left portion
# it it bigger then we should seach in right portion
