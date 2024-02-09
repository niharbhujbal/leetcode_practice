class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        max_len = 1
        seq_len = 1
        current = nums[0]
        for i in nums[1:]:
            if current == i - 1:
                seq_len += 1
            else:
                max_len = max(seq_len, max_len)
                seq_len = 1
            current = i
        return max(max_len, seq_len)


# first we will sort the list that takes nlog(n)
# then we will record which sequence holds for max length
