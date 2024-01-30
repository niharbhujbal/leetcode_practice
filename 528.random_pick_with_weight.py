import bisect
import random
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.traget_field = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.traget_field.append(self.total)

    def pickIndex(self):
        """
        :rtype: int
        """
        random_no = self.total * random.random()
        return bisect.bisect_left(self.traget_field, random_no)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# we can think that we will create an array with field with target field from 0 to total sum of the array
# if we allocate  percentage region based on weight
# then we just have to create a random no between 0-1 and scale that no to our array
# the just do binary search to find index at which this no can fit
