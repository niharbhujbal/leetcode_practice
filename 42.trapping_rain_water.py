class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # create two arrays one with max height on left side and second with max value on right side
        # at a specific water trapping will be max of heights from both sides and depth of the height
        
        left_max = []
        max_height = 0
        for i in height:
            max_height = max(max_height, i)
            left_max.append(max_height)

        right_max = []
        max_height = 0
        for i in height[::-1]:
            max_height = max(max_height, i)
            right_max.append(max_height)
        right_max = right_max[::-1]

        trapped_water = 0
        for i, h in enumerate(height):
            trapped_water += min(left_max[i], right_max[i]) - h

        return trapped_water
    
        # 2 pointers
    
        # areas = 0
        # max_l = max_r = 0
        # l = 0
        # r = len(height) - 1
        # while l < r:
        #     if height[l] < height[r]:
        #         if height[l] > max_l:
        #             max_l = height[l]
        #         else:
        #             areas += max_l - height[l]
        #         l += 1
        #     else:
        #         if height[r] > max_r:
        #             max_r = height[r]
        #         else:
        #             areas += max_r - height[r]
        #         r -= 1
        # return areas
