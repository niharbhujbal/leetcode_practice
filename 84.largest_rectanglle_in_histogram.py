class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0

        stack = []
        for index_, height in enumerate(heights):
            if len(stack) == 0 or stack[-1][-1] < height:
                stack.append((index_, height))
            elif stack[-1][-1] > height:
                while len(stack) > 0 and stack[-1][-1] > height:
                    top_ind, top_height = stack.pop()
                    max_area = max(max_area, top_height * (index_ - top_ind))
                stack.append((top_ind, height))

        for left_bound, height in stack:
            max_area = max(max_area, height * (len(heights) - left_bound))

        return max_area


# we want to use monotonic increasing stack
# we keep add the value of index and height at the index to stack
# while adding compare element to top of stack add if current is larger
# if the current is smaler than top then keep poping from stack and calculate the area by sbtracting current index and that element index
# keep the max area in check
# if we poped the element the store the index of last poped element with current element
# after we are done we have monotonic incresing stack in stack
# all the elements in stack can extend till end of array
# so compute area for each and check max return max at the end


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # found the min height and index
        min_height = 1e5
        min_index = -1
        for ind, val in enumerate(heights):
            if min_height > val:
                min_height = val
                min_index = ind
        # max area for this length
        area = min_height * len(heights)
        # now divide
        # left side
        if len(heights[:min_index]) > 0:
            left_area = self.largestRectangleArea(heights[:min_index])
        else:
            left_area = 0
        if min_index + 1 < len(heights):
            right_area = self.largestRectangleArea(heights[min_index + 1 :])
        else:
            right_area = 0
        return max(area, left_area, right_area)


# get min in the array
# then max area it can have is min of the array * length
# then divide the array into two parts left side of the min and right side of the min
# again run same algo on the array
# stop condition of reccursion is when the left and right side of the min is zero
