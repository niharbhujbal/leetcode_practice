class Solution:
    def minimumSwaps(self, nums):
        min_val, min_in = float("inf"), len(nums)
        max_val, max_in = float("-inf"), 0
        for ind, i in enumerate(nums):
            if i < min_val:
                min_val, min_in = i, ind
            if i >= max_val:
                max_val, max_in = i, ind

        total = min_in
        total += len(nums) - max_in - 1
        if min_in > max_in:
            total -= 1
        return total
