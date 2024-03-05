import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        no_of_sub_array = 0
        sum_hashmap = collections.defaultdict(int)
        sum_ = 0
        sum_hashmap[0] += 1

        for i in nums:
            sum_ += i
            compliment = sum_ - k
            if compliment in sum_hashmap:
                no_of_sub_array += sum_hashmap[compliment]
            sum_hashmap[sum_] += 1

        return no_of_sub_array


# we have to create a hashmap of sums till the current element that we are iterating
# hashmap will have the sum and no of times the sum is occuring
# we will have to add 0 to check if the element added in sum == k ie it will create a sub array of length 1 with sum k
# we keep adding the sun in hashmap and incrementing the no of times that sum occurs
