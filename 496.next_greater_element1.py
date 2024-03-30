class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3 = [-1] * len(nums2)
        stack = []
        for ind, val in enumerate(nums2):
            if not stack:
                stack.append((ind, val))
            else:
                while stack and stack[-1][-1] < val:
                    ind_, _ = stack.pop()
                    nums3[ind_] = val
                stack.append((ind, val))
        hashmap = {}
        for ind, val in enumerate(nums2):
            hashmap[val] = nums3[ind]

        ans = []
        for i in nums1:
            ans.append(hashmap[i])
        return ans


# make an array with -1 of length num2
# change all the greatest array using num2 and monotonic stack
# make a hashmap with value in the nums2 and key as next greatest element
# now just iterate though num1 and replace with haspmap values
