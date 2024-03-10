class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        target_array = [0] * target
        for p, s in zip(position, speed):
            target_array[p] = s
        stack = []
        for ind, val in enumerate(target_array):
            if val == 0:
                continue
            distance = target - ind
            time = float(distance) / float(val)
            if len(stack) == 0:
                stack.append(time)
            else:
                while stack[-1] <= time:
                    stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(time)
        return len(stack)


# create a monotonic stack of time it takes to reach to target
# upend the time if stack is empty
# else compare the element at the top keep removing the element if the element is smaller or equal to time and at the end append the element
# repeat the process and you will have all the fleets in the stack at the end so we just need how many fleets were there
