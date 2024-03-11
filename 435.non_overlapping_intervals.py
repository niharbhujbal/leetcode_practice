class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], x[1] - x[0]))

        merged = []
        count = 0
        for inte in intervals:
            if len(merged) == 0 or merged[-1][1] <= inte[0]:
                merged.append(inte)
            else:
                count += 1
                # keep the interval which ends first
                if merged[-1][1] > inte[1]:
                    merged.pop()
                    merged.append(inte)
        return count
