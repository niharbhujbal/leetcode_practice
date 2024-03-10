class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        answer = 0
        counts = {0: 0, 1: 0}

        for right, num in enumerate(nums):
            counts[num] += 1

            while counts[0] > k:
                counts[nums[left]] -= 1
                left += 1

            curr_window_size = right - left + 1
            answer = max(answer, curr_window_size)

        return answer


# start with left and right and 0
# keep increasing the right pointer until k value is 2
# once condition is met get max length
# reduce the left pointer until the condition is unment
# the again increase the right pointer until it meets
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
#      l
#                      r
