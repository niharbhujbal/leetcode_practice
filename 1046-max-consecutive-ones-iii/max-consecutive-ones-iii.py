class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        zeros = 0
        max_len = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            max_len = max(r - l + 1, max_len)
        return max_len
            