from collections import Counter


class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = Counter(arr)
        heap = []
        for k, v in c.items():
            heapq.heappush(heap, (k, v))
        max_val = 0
        while heap:
            k, v = heapq.heappop(heap)
            max_val += min(k - max_val, v)

        return max_val


# we will create value and its count dictonary
# then create min heap with value
# then will run a while loop while heap becomes empty
# we will track max value
# there two possiblities to increase the max value
# either cout of element is less than the difference between value and prev max value
# then we have to increse all the element till the count
# or count is more and then we can just increse the element till value of element so we just add the diff
