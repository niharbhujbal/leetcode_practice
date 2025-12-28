class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def bt(ind,seq):
            nonlocal n
            if ind == n:
                ans.append(seq)
                return
            for i in nums:
                if i not in seq:
                    bt(ind+1, seq+[i])
        
        bt(0,[])
        return ans