class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        def backtrace(nums, result, total):
            nonlocal target
            if total == target:
                ans.add(tuple(result))
            elif total > target:
                return
            else:
                for ind, val in enumerate(nums):
                    backtrace(nums[ind:], result + [val], total + val)

        backtrace(candidates, [], 0)
        return ans


# here each position has choice of all the elements and not including any element
# but passing to next recusrrsion just remove the the elements before that
