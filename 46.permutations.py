class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        self.dfs([], nums, set(), res)
        return res

    def dfs(self, sol, nums, traversed_set, res):
        if len(sol) == len(nums):
            res.append(sol)
        else:
            for i in nums:
                if i not in traversed_set:
                    traversed_set_temp = set(traversed_set)
                    traversed_set_temp.add(i)
                    self.dfs(list(sol + [i]), nums, traversed_set_temp, res)


# each time we have all the values in nums
# for next position we don't include the element and choose from remaining elements
