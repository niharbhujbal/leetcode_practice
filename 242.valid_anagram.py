class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for char in s:
            if char in hashmap.keys():
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            if char in hashmap.keys():
                if hashmap[char] == 1:
                    del hashmap[char]
                else:
                    hashmap[char] -= 1
            else:
                return False
        return len(hashmap) == 0


# we will create one hashmap
# create letter as key and no of time that letter appears as a value
# loop over first string and create the hashmap
# now we will loop over the second string
# if the letter is in dictonary then decrease the count of that letter by one and if the count goes to zero then delete the pair
# if the key is not in the dictonary then retun false
# at the end check if the dictonary is empty if true then it is a anagram else not an anagram
