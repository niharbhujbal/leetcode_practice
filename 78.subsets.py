class Solution:
    def subsets(self, nums):
        ans = []

        def backtrace(result, pointer):
            if pointer >= len(nums):
                ans.append(result)
            else:
                backtrace(result + [nums[pointer]], pointer + 1)
                backtrace(result, pointer + 1)

        backtrace([], 0)
        return ans


# create a answer list
# we create a backtrace function which creates result and a pointer
# idea here is every elment has two option either be in the result or not
# so termination condition will be if the pointer goes beyond nums
# and pointer will incremenet from 0
# for each element we will call back trace twice in one we will include the element and in the second we won't include the element
