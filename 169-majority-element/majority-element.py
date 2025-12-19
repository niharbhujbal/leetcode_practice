class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's algo
        change_ele = True
        for i in nums:
            if change_ele:
                ele = i
                count = 1
                change_ele = False
                continue
            if i == ele:
                count += 1
            else:
                count -= 1
            if count == 0:
                change_ele = True
        
        return ele