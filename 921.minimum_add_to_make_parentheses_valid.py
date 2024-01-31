class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        stack_size = 0
        count_ = 0
        for p in s:
            if p == "(":
                stack.append(p)
                stack_size += 1
            else:
                if len(stack) == 0:
                    count_ += 1
                else:
                    stack.pop()
                    stack_size -= 1

        return stack_size + count_


# iterate over the string
# if ( then push it to stack
# if ) and stack is empty the we have to add one ( so increase counter
# if stack is not empty then just pop one item
# at the end return the sum
