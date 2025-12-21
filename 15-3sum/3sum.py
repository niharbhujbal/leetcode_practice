class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            target = -nums[i]
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ == target:
                    a = [nums[i],nums[l],nums[r]]
                    a.sort()
                    ans.add(tuple(a))
                    r -= 1
                elif sum_ > target:
                    r -= 1
                elif sum_ < target:
                    l += 1
            
        return list(ans)


