class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        string = ""
        par_counter = {"(": 0, ")": 0}
        return self.genpar("", n, par_counter)

    def genpar(self, string, n, par_couner):
        if self.validate_par(string):
            if par_couner["("] == n and par_couner[")"] == n:
                return [string]
            elif par_couner["("] > n or par_couner[")"] > n:
                return []
            else:
                par_couner1 = par_couner.copy()
                par_couner1["("] += 1
                ans1 = self.genpar(string + "(", n, par_couner1)
                par_couner2 = par_couner.copy()
                par_couner2[")"] += 1
                ans2 = self.genpar(string + ")", n, par_couner2)
                # if valid then return i list
                return ans1 + ans2
        else:
            return []

    def validate_par(self, s):
        pair = {")": "("}
        stack = []
        for i in s:
            if i == "(":
                # when left bracket appear push it to stack
                stack.append(i)
            elif i == ")":
                # when left bracket apper pop from stack
                if len(stack) > 0 and pair[i] == stack.pop():
                    continue
                else:
                    return False

        # compare that its a pair
        # if the not then return false
        # if yes the move forward
        return len(stack) == 0 or ")" not in stack
    
# Generate a back tracing function which creates combination of the paranthesis
# every position has two posiblities 
# but before going further check if the
