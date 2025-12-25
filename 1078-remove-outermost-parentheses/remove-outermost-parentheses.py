class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""
        for ind, par in enumerate(s):                
            if par == "(":
                if len(stack) != 0:
                    ans += "("
                stack.append("(")
            else:
                stack.pop()
                if len(stack) != 0:
                    ans += ")"
        return ans
