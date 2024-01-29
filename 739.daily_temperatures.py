class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for ind, val in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((ind, val))
            else:
                while stack[-1][-1] < val:
                    top_index = stack[-1][0]
                    ans[top_index] = ind - top_index
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append((ind, val))
        return ans


# intialise an stack
# create a ans array of length temprature with zeros
# check the stack if empty then push the elemnt with its index to stack
# the move to next element peak the top elemet of the tsack if the element of on top is smaller than stack
# then subtract the differene of element and top index and store it to index of top element
# then pop the top element and put the element in
# we should keep poping the elements until we get an element greater than the element
