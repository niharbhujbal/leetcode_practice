class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_val = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            # left sorted
            min_val = min(nums[left], nums[right], nums[mid], min_val)
            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                else: 
                    left = mid + 1
            # right sorted
            else:
                if nums[left] < nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1
        return min_val