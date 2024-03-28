class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_non_zeros = set(nums) - {0}
        return len(unique_non_zeros)


# since we have to all the same no are gonna be zero at the same time we just have to count unique nos that are not zero
