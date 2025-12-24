class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        # ceil operation in this we are searching from min in array to max of array
        # max sum to low sum
        # min val to max val
        # so binary seach condition should be <=
        left = 1
        right = max(nums)
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            sum_ = sum([math.ceil(i/mid) for i in nums])
            if sum_ <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans