class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # calculate how many hours it would take to finish all the bananas if koko had spped of k
        # koko_hours = sum([math.ceil(float(i) / k) for i in piles])
        # binary search for h
        left = 1
        right = max(piles)
        k = -1
        while left <= right:
            mid = left + (right - left) // 2
            koko_hours = sum([math.ceil(float(i) / mid) for i in piles])
            if koko_hours <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k
            