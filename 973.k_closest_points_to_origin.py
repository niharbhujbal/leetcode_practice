import collections, math, heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, (x, y)))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(list)
        h = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            d[dist].append([x, y])
            heapq.heappush(h, dist)
        ans = []
        while len(ans) < k:
            ans.extend(d[heapq.heappop(h)])
        return ans


# create a heap with distance as key and index of the that point as an values
# now just get the top k points and return them
