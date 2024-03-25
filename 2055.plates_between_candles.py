import bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_indices = []
        for ind, char in enumerate(s):
            if char == "|":
                candle_indices.append(ind)
        ans = []
        for start, end in queries:
            left_most = bisect.bisect_left(candle_indices, start)
            right_most = bisect.bisect_right(candle_indices, end)
            if left_most < right_most:
                left_most_candle = candle_indices[left_most]
                right_most_candle = candle_indices[right_most - 1]
                total_chars_len = len(s[left_most_candle : right_most_candle + 1])
                total_candle_in_range = right_most - left_most
                ans.append(total_chars_len - total_candle_in_range)
            else:
                ans.append(0)
        return ans


# create an array which indicates all the indices of candles
# get start and end of the query
# do a binary search and try to fit start and end in the array
# left most candle will be represented by ans of binary search of start and right most will be represnted by the ans of binary search of right -1
# so just take pos of right most and pos left most candle and subtract no of candles in that sub portion of array
