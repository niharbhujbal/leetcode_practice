class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        nums.sort()
        n = len(nums)
        def bt(ind,ss):
            nonlocal n
            if ind == n:
                subsets.add(tuple(ss))
                return
            
            # no pick
            bt(ind+1, ss)
            # pick
            bt(ind+1, ss +[nums[ind]])
        bt(0,[])
        return list(subsets)
            
            