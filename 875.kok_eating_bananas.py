import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        min_k = 1
        max_k = max(piles) + 1
        return self.binary_seach_k(min_k, max_k, piles, h)

    def binary_seach_k(self, start, end, piles, h):
        mid = (start + end) // 2
        piles_h = [-(-i // mid) for i in piles]
        sum_pile = int(sum(piles_h))
        if sum_pile == h:
            return mid
        elif sum_pile > h:
            return self.binary_seach_k(mid, end, piles, h)
        elif sum_pile < h:
            return self.binary_seach_k(start, mid, piles, h)


# max bananas koko can eat is max value in the array
# so he can each bananas in len(piles) hours
# min he can eat is 1 so it will tak him sum(piles) hours
# k range(1,max(p)+1)
# we have to add
# brute force way is to go in linear fashion but we can perfor binary search to get the value of k
# we will create a new function with range of k and piles and h
# once we find mid of range
# devide with k to every element with ceil operator and take sum of the array
# if sum > h then  new range is mid to end
# if sum < h the new range start to mid
