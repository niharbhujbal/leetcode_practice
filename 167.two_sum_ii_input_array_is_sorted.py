class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i,j in enumerate(numbers):
            if target-j in hm:
                return [hm[target-j],i+1]
            else:
                hm[j] = i+1

# even if the array is sorted we will use the same two sum solution