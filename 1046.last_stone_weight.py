import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if x == y:
                continue
            else:
                heapq.heappush(max_heap, -(x - y))

        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0


# create a max heap of the stones
# pop two largest items from heap and calulate then push the stone into heap
