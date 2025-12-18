class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of first 1 to n
        n = len(nums)
        sum_n = n * (n + 1) // 2
        sum_nums = sum(nums)

        # only remaining number will be number which is not present
        return sum_n - sum_nums