class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        ans = {}
        for ind, i in enumerate(nums[:-2]):
            target = 0 - i
            returned_tuple = self.Twosum(target, nums[ind + 1 :])
            if returned_tuple is None:
                continue
            else:
                for j in returned_tuple:
                    ans[tuple(sorted([i, j[0], j[1]]))] = None
        return [list(i) for i in ans.keys()]

    def Twosum(self, target, array):
        ans = []
        hm = set()
        for i in array:
            if target - i in hm:
                ans.append((target - i, i))
            else:
                hm.add(i)
        if len(ans) == 0:
            return None
        else:
            return ans


# here solution is fix one element and apply two sum on remaining element
# so iterate over the array and store all the solutions
