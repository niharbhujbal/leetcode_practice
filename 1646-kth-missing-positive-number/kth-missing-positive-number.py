class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        p = 0
        nos =  set(arr)
        missing = 0
        while missing < k:
            p += 1
            if p not in nos:
                missing += 1
        return p

