class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        max_len = 0
        char_indexs = {}
        for char in s:
            if char not in char_indexs.keys() or (char in char_indexs.keys() and char_indexs[char] < left):
                char_indexs[char] = right
            else:
                left = char_indexs[char] + 1
                char_indexs[char] = right
            right += 1
            max_len = max(right - left, max_len)
        return max_len
    
# intialise the left and right pointer at 0 index
# hashmap of charcter and it index will be saved
# for loop over the string
# if the character is in hashmap then stro the max length
# move left to char index + 1
# and update the new character index
# if the not in index then increment right and length
# and add the char to hashmap