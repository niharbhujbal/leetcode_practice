class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        majority_count = len(nums) // 2
        for element in nums:
            counter[element] += 1
            if counter[element] > majority_count:
                return element
        
        return 0