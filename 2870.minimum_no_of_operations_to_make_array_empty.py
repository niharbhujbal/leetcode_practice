class Solution:
    def minOperations(self, nums):
        from collections import Counter

        mp = Counter(nums)

        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1

        return count


# count the no of time a no has occured
# 1 > not possible
# 2 > 1
# 3 > 1
# 4 > 2
# 5 > 2
# 6 > 2
# 7 > 3
# we are dividing count by 3 and getting ceil value of divided value
