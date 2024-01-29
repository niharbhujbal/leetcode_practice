class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        non_zero = {}
        for ind, val in enumerate(nums):
            if val != 0:
                non_zero[ind] = val
        self.non_zero = non_zero

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        # intersectionset = set(self.non_zero.keys()).intersection(set(vec.non_zero.keys()))
        sum = 0
        for i in set(self.non_zero.keys()).intersection(set(vec.non_zero.keys())):
            sum += self.non_zero[i] * vec.non_zero[i]
        return sum


# so we first store all the non zero elements in the hashmap
# the create a intersection of both non zero elements
# iterate over those elements and get the sum of those
