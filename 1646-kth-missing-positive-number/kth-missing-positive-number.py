class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = k
        for i in arr:
            if i <= missing:
                missing += 1
            else:
                continue
        return missing


