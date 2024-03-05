import random, collections


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.hashmap = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.hashmap[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        rand_val = random.randint(0, len(self.hashmap[target]) - 1)
        return self.hashmap[target][rand_val]


# create a hashmap of all the indexes for a value
# then generate a random value between 0 - length of possible values
# return index at that value

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
