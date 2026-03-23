class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        g = g[::-1]
        s.sort()
        s = s[::-1]

        output = 0
        i,j = 0,0 
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                output += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                i += 1
        return output
        