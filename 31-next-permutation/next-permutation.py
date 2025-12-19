class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        # move from right to left check if any of the elements of right are larger than current elementif there is then that is break point
        break_point_pointer = len(nums) - 1
        max_element = nums[break_point_pointer]
        while break_point_pointer >= 0:
            if nums[break_point_pointer] < max_element:
                break
            max_element = nums[break_point_pointer]
            break_point_pointer -= 1
        
        if break_point_pointer < 0:
            nums.sort()
            return

        # when you find the break point replace it with number greater than break element
        next_greater_element = max_element
        ind = break_point_pointer + 1
        for ele in nums[break_point_pointer+1:]:
            if ele > nums[break_point_pointer]:
                if ele <= next_greater_element:
                    next_greater_element = ele
                    next_greater_element_index = ind
            ind += 1 
        nums[break_point_pointer], nums[next_greater_element_index] = nums[next_greater_element_index], nums[break_point_pointer]
        self._reverse_range_in_place(nums, break_point_pointer+1, len(nums)-1)
        
    def _reverse_range_in_place(self, values: List[int], left: int, right: int) -> None:
        """Reverse values[left:right+1] in-place."""
        while left < right:
            values[left], values[right] = values[right], values[left]
            left += 1
            right -= 1
        
        # place remaining elements in sorted order
