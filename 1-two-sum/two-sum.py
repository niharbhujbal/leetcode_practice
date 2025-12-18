class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_ = {}
        for ind, ele in enumerate(nums):
            comp = target - ele
            if comp in sum_:
                return sum_[comp], ind
            sum_[ele] = ind
