import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


# create a min heap
# keep pushing the one by one element to the heap and if the heap size increase tha k size then we pop element from the heap
# so at the end we only have heap of k largest elements and the first element will the kth largest
