from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        nge = len(nums2) * [-1]
        position_map = {}
        for ind, ele in enumerate(nums2):
            if len(stack) != 0 and stack[-1][1] < ele:
                while len(stack) != 0 and stack[-1][1] < ele:
                    nge[stack[-1][0]] = ele
                    stack.pop()
            stack.append((ind,ele))
            position_map[ele] = ind
        ans = []
        for i in nums1:
            ans.append(nge[position_map[i]])
        return ans
        