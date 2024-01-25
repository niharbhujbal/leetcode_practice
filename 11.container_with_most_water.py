class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # first intialise the two pointer at start and end of the pointer
        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        # then calculate the area of container
        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            # save that rate in a hash map with pair of points that formed the area
            if area > max_area:
                max_area = area
            # then check which buildeing is min and move that pointer to respective positions
            if height[p1] < height[p2]:
                p1 += 1
            elif height[p1] > height[p2]:
                p2 -= 1
            # if the height is same then
            elif height[p1] == height[p2]:
                if height[p1 + 1] < height[p2 - 1]:
                    p1 += 1
                else:
                    p2 -= 1
        return max_area
