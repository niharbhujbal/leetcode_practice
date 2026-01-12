from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        hashmap = defaultdict(list)
        i = 0
        # down - True
        # up - False
        dire = True
        for char in s:
            if i < 0:
                dire = True
                i += 2
            if i >= numRows:
                dire = False
                i -= 2
            hashmap[i].append(char)
            if dire:
                i += 1
            else:
                i -= 1
        ans = []
        for i in range(numRows):
            ans.extend(hashmap[i])
        return "".join(ans)