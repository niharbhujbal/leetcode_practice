import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.defaultdict(int)
        top_freq = 0
        for num in nums:
            counter[num] += 1
            if counter[num] > top_freq:
                top_freq = counter[num]

        freq = collections.defaultdict(list)
        for num, frequency in counter.items():
            freq[frequency].append(num)

        ans = []
        for i in range(top_freq, len(freq) - k, -1):
            ans.extend(freq[i])

        return ans[:k]


# create counter and store the top frequecy
# then inverse dictonary of frequecy to list of intergers that occured that many times
# create a answer with k items
