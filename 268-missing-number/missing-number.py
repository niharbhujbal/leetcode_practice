class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_numer = set(range(0,len(nums)+1)) - set(nums)
        return list(missing_numer)[0]