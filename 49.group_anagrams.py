import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_group = collections.defaultdict(list)
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord("a")] += 1
            anagram_group[tuple(key)].append(string)

        return anagram_group.values()


# create a hashmap
# convert all the words to a tuple of 26 letter with count of occurance of each letter in respective position
# add that letter to list of that key
# at the end just get all the lists
