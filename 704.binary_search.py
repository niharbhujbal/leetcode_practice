class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(0, len(nums), nums, target)

    def binary_search(self, start, end, array, target):
        mid = (start + end) / 2
        mid = int(mid)
        if array[mid] == target:
            return mid
        elif start == mid:
            return -1
        elif target < array[mid]:
            return self.binary_search(start, mid, array, target)
        else:
            return self.binary_search(mid, end, array, target)


# a seprate function which get start index and end index and array and target
# add the start and end and div by 2
# round the no to nearest integer if
# you will get middle index
# go to that index and check if it match the taget
# if not whether the value is smaller or larger than taget
# according to that call the functio reccursively with modified bounds
