class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set(range(0,len(nums)+1)) - set(nums)
        return list(a)[0]