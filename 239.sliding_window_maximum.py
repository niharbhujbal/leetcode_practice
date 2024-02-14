class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = collections.deque()
        l = 0
        r = 0
        ans = []
        while r < k:
            if len(dq) == 0:
                dq.append(nums[r])
                r += 1
            elif dq[-1] < nums[r]:
                dq.pop()
            else:
                dq.append(nums[r])
                r += 1
        ans.append(dq[0])

        while r < len(nums):

            if nums[l] == dq[0]:
                dq.popleft()
            l += 1
            if len(dq) == 0:
                dq.append(nums[r])
                r += 1
            else:
                while len(dq) != 0 and dq[-1] < nums[r]:
                    dq.pop()

                dq.append(nums[r])
                r += 1
            ans.append(dq[0])
        return ans


# We will use monotonically decreasing queue
# first we will create monotinically decreasing queue with first k elements
# elements which come befoe the max elements don't matter even if they are second largest because
# they will fall out of the window before the max element so they will never be max element in any of the windows
# create two pointers left and right
