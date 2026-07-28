class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindx = 0
        for ind, ele in enumerate(nums):
            print(maxindx, ind, ele)
            if maxindx < ind:
                return False
            maxindx = max(maxindx, ind+ele)
        return maxindx >= len(nums) - 1 
