class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        i = 0
        for ind, ele in enumerate(nums):
            if ele != 0:
                nums[i] = ele
                i += 1
            else:
                zeros += 1
        
        for j in range(zeros):
            nums[i+j] = 0
        
        return nums