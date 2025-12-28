class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        ans = []
        def bt(ind, sum_, seq):
            nonlocal k,n
            if len(seq) == k and sum_ == n:
                ans.append(seq)
                return
            if ind == len(nums) or len(seq) > k or sum_ > n:
                return
            # not pick
            bt(ind+1 , sum_ , seq)
            # pick
            bt(ind+1 , sum_ + nums[ind], seq + [nums[ind]])
        bt(0,0,[])
        return ans
        