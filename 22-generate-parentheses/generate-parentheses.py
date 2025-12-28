class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(seq,l,r):
            nonlocal n
            if l == n and r == n:
                ans.append(seq)
            
            # you can add as many left's
            if l < n:
                backtrack(seq+"(",l+1,r)
            # right brackets has to be less than 1
            if r < n and r+1 <= l:
                backtrack(seq+")",l,r+1)

        backtrack("",0,0)
        
        return ans    
        

