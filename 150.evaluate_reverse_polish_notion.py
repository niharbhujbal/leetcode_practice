class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        signs = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in signs:
                stack.append(int(i))
            elif i in signs:
                num1 = stack.pop()
                num2 = stack.pop()
                if i == "+":
                    exp_ans = num2 + num1
                if i == "-":
                    exp_ans = num2 - num1
                if i == "/":
                    exp_ans = float(num2) / float(num1)
                if i == "*":
                    exp_ans = num2 * num1
                stack.append(int(exp_ans))
        return sum(stack)


# Create a stack
# keep pushing the values until you encounter a sign
# check with is numif the sign is + - then pop from stack the pop two element do operation and push it to stack
# if you encounter a * or / sign the pop 2  elemtent of the and do the operation then push it to stack
# at the end sum sum the stack and return the value
#
