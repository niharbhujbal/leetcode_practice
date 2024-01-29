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
