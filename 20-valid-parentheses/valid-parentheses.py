from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # create a stack
        pair = {'(':')','[':']','{':'}'}
        stack = deque()
        for i in s:
            if i  in pair.keys():
        # when left bracket appear push it to stack
                stack.append(i)
            else:
        # when left bracket apper pop from stack
                if len(stack) > 0 and pair[stack.pop()] == i:
                    continue
                else:
                    return False
        
        # compare that its a pair
        # if the not then return false
        # if yes the move forward
        return len(stack) == 0
        
        # at the end check if stack is empty
        # if empty then return true else false