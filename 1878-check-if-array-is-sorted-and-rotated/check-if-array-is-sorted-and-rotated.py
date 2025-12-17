class Solution:
    def check(self, nums: List[int]) -> bool:
        # if length is 1 then return true
        # then start the pointer from index 1 to end of array
        # compare i and i - 1 element
        # checks += 1 if i >= i-1
        # return checks <= 1
        # we want check last and fiest element so as to do a circular check
        if len(nums) == 1:
            return True
        
        drops = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                drops += 1
        if nums[-1] > nums[0]:
            drops += 1
        print(drops)
        return drops <= 1