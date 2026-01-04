from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = [-1] * len(nums)
        stack = deque()
        for i in range(2):
            for ind, val in enumerate(nums):
                if stack:
                    while stack and stack[-1][-1] < val:
                        ind_, _ = stack.pop()
                        nums2[ind_] = val
                stack.append((ind, val))
        return nums2