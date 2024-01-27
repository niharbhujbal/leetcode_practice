class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow1 = 0
        slow2 = 0
        fast = 0
        # we know there going to be a cycle so lets find intersection of slow and fast pointer
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break

        # we found the intersection point now lets find the start of cycle
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1
