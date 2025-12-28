class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
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
            
            # pick
            backtrace(ind+1, sum_+candidates[ind], res+[candidates[ind]])
            # not pick
            new_ind = ind
            while new_ind < n and candidates[ind] == candidates[new_ind]:
                new_ind += 1
            if new_ind < n:
                backtrace(new_ind, sum_, res)
        
        backtrace(0,0,[])
        return list(ans)