import heapq


class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.min_value is None or val < self.min_value:
            self.min_value = val
        self.stack.append((val, self.min_value))

    def pop(self):
        """
        :rtype: None
        """
        pop_Val = self.stack[-1][0]
        self.stack = self.stack[:-1]
        if len(self.stack) == 0:
            self.min_value = None
        else:
            self.min_value = self.stack[-1][1]
        return pop_Val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# each value will have its ouwn min value
# intiate a min value as None
# when pushing an elemnt to the stack
# check if then element is smaller than min value if none the directly assign the value
# and push tuple of min value and val to stack
# for pop will jus return the last element and update the min value for element after that
# if stack is empty now then just assign null value to min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
