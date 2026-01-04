from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack)== 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        element = self.stack.pop()
        if element == self.min_stack[-1]:
            self.min_stack.pop()
        return element

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()