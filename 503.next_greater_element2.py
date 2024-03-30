class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = [-1] * len(nums)
        stack = []
        for i in range(2):
            for ind, val in enumerate(nums):
                if not stack:
                    stack.append((ind, val))
                else:
                    while stack and stack[-1][-1] < val:
                        ind_, _ = stack.pop()
                        nums2[ind_] = val
                    stack.append((ind, val))
        return nums2


# we create a nums2 array with -1 value and length of nums array
# the we create a monotonic stack and find the next greatest element and replace it
# here we want to loop over the array one more time like a circular array
# so we run the code twice
