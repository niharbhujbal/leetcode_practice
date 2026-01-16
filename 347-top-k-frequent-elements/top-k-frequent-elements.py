class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        heap = []
        for i in nums:
            counter[i] += 1
        for i, j in counter.items():
            heapq.heappush(heap,(j, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [j for i,j in heap][::-1]
