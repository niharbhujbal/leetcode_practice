import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        self.H = nums
        self.k = k
        while len(self.H) > k:
            heapq.heappop(self.H)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.H, val)
        k = self.k
        while len(self.H) > k:
            heapq.heappop(self.H)

        return self.H[0]
