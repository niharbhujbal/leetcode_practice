class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # create a stack
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                # when left bracket appear push it to stack
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                # when left bracket apper pop from stack
                if len(stack) > 0 and pair[i] == stack.pop():
                    continue
                else:
                    return False

        # compare that its a pair
        # if the not then return false
        # if yes the move forward
        return len(stack) == 0

        # at the end check if stack is empty
        # if empty then return true else false
