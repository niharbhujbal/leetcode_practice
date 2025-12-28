class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def backtrace(ind, sum_, res):
            nonlocal n
            if sum_ == target:
                ans.append(res)
                return
            elif sum_ > target:
                return
            if ind == n:
                return
            
            # not pick
            backtrace(ind+1, sum_, res)
            # pick
            backtrace(ind, sum_+candidates[ind], res+[candidates[ind]])
        
        backtrace(0,0,[])
        return ans
        
            

