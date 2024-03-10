class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index_, element in enumerate(nums):
            comp = target - element
            if comp in hashmap:
                return [index_, hashmap[comp]]
            else:
                hashmap[element] = index_


# create a hashmap
# loop over the array
# get the element and its index
# computer the complimnet ie target - the value
# if the compliment is in hashmap then retun indexes else add the element to hashmap
