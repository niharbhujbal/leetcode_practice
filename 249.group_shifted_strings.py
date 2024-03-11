from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        storage = defaultdict(list)

        for s in strings:
            key = []
            for i in range(len(s) - 1):
                # keep the values in negative gives correct values when taking the differenece
                diff = ord(s[i]) - ord(s[i + 1])
                diff = diff % 26
                key.append(diff)

            storage[tuple(key)].append(s)
        return storage.values()
