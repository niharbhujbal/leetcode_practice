class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res_set = set()

        def dfs(result, nums):
            if len(nums) == 0:
                res_set.add(tuple(result))
            else:
                nums_temp = list(nums)
                first_ele = nums_temp.pop(0)
                dfs(result, nums_temp)
                dfs(result + [first_ele], nums_temp)

        dfs([], sorted(nums))

        return list(res_set)


# create a result set
# create a dfs funciton where it has two choices add the first element from nums or don't
# if the nums is empty the add the result to result set
