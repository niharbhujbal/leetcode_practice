class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index_, i in enumerate(nums):
            if target - i in hashmap:
                return hashmap[target - i], index_
            else:
                hashmap[i] = index_