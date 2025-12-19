class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for ele in nums:
            if ele < 0:
                negative.append(ele)
            elif ele >= 0:
                positive.append(ele)
        
        write_p = 0
        while write_p < len(nums):
            nums[write_p] = positive[write_p//2]
            write_p += 1
            nums[write_p] = negative[write_p//2]
            write_p += 1
        return nums