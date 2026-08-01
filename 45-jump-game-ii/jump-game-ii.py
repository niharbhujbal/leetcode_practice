class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        l = 0
        r = l+1
        while r < len(nums):
            l, r = r, max([nums[i] + i for i in range(l,r)]) + 1
            jumps += 1
        return jumps

# [2,3,1,1,4]
#        l
#            r