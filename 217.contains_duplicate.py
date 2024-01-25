class Solution:
    def containsDuplicate(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False


# We will create a set
# iterate over the list and if the element is in set then return True
# else add that element into set
# at the end if loop completes then there are no duplicates
