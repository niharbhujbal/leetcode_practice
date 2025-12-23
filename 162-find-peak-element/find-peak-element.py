class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)      
        left  = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # check peak element
            if (mid == 0 or nums[mid - 1] < nums[mid]) and ( mid == n-1 or nums[mid] > nums[mid + 1]):
                return mid
            # peak is on right
            if (mid == 0 or nums[mid - 1] < nums[mid]) and ( mid == n-1 or nums[mid] < nums[mid + 1]):
                left = mid + 1
            else:
                right = mid - 1
        