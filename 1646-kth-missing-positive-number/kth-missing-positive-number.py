class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # for each index is array we can find how many are missing ele - 1 - index
        # arr[i] - i
        # by binary search figure out no of <= k

        # array start after k
        if arr[0] - 1 >= k:
            return k
        n = len(arr)
        # answer is beyonf last element
        if (arr[n-1] - (n-1) - 1) < k:
            return arr[n-1] + k - (arr[n-1] - (n-1) - 1)

        left = 0
        right = len(arr) - 1
        corr_ind = right
        while left <= right:
            mid = left + (right - left) // 2
            missing_count = arr[mid] - mid - 1
            if missing_count < k:
                corr_ind = mid
                missing_c = missing_count
                left = mid + 1 
            else:
                right = mid - 1
            
        return arr[corr_ind] + (k- missing_c)

