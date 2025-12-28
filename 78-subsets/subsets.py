class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrace(ind,sol):
            nonlocal n
            if ind == n:
                ans.append(sol)
                return
            
            # not take
            backtrace(ind+1, sol)
            # take
            backtrace(ind+1, sol+[nums[ind]])
        
        backtrace(0,[])
        return ans
            
