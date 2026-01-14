from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [""] * numRows
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
            ans[i] += char
            if dire:
                i += 1
            else:
                i -= 1

        return "".join(ans)