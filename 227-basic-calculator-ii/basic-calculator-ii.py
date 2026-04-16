class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        sign = {'+','-',"*",'/'}
        prev_sign = '+'
        number = 0
        for ind, i in enumerate(s):
            if i.isdigit():
                number = number * 10 + int(i)
            
            if i in sign or ind == len(s) - 1:
                if prev_sign == '+':
                    stack.append(number)
                if prev_sign == '-':
                    stack.append(-1*number)
                if prev_sign == '*':
                    stack.append(int(stack.pop() * number))
                if prev_sign == '/':
                    stack.append(int(stack.pop() / number))
                prev_sign = i
                number = 0
  
        return int(sum(stack))

                