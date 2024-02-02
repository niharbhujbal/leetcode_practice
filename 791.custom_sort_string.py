from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(list(s))
        ans = ""
        for char in order:
            if char in count:
                for _ in range(count[char]):
                    ans += char
                del count[char]

        for key, val in count.items():
            for _ in range(val):
                ans += key
        return ans


# we will create a counter of string s
# and we will iterate through order and will add that order string no of times it has occured and delete that letter from counter
# loop this for all order
# now loop through counter add add remaining elements
