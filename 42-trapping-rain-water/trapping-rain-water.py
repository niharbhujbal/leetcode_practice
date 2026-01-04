class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        area = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # we know there is something bigger on right so left max will decide how much water they are storing
            if left_max <= right_max:
                area += left_max - height[left]
                left += 1
            else:
                area += right_max - height[right]
                right -= 1
        return area


# i will keep a left and right pointer
# can keep running of left max and right max
# we will check if left height is bigger or the right max is bigger
# according the that the water will be calculated by the other side