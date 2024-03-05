class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        stack = []

        for i, h in enumerate(heights):
            if len(stack) == 0:
                pass
            else:
                while heights[stack[-1]] <= h:
                    stack.pop()
                    if len(stack) == 0:
                        break
            stack.append(i)

        return stack


# we have to create a montonic decreasing stack
# so that we will know which building can see over other buildings


class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_height = 0
        building_with_views = []
        index = len(heights)
        for building_height in heights[::-1]:
            index -= 1
            if building_height > max_height:
                building_with_views.append(index)
                max_height = building_height
            else:
                continue
        return building_with_views[::-1]


# iterate the array from back and store the max value
# if compare the value with max value
# if max value changes then that building has ocean view and update max value
# if not just continue
