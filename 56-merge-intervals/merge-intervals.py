class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda x : x[0])
        for i in intervals:
            if len(ans) == 0:
                ans.append(i)
            elif ans[-1][1] >= i[0]:
                ans[-1][1] = max(i[1],ans[-1][1])
            else:
                ans.append(i)
        return ans

