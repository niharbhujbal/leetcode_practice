class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        array = [0] * 26
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            array[ord(s[right]) - ord("A")] += 1
            right += 1
            if right - left - max(array) <= k:
                max_len = max(right - left, max_len)
                continue
            else:
                while left < right:
                    array[ord(s[left]) - ord("A")] -= 1
                    left += 1
                    if right - left - max(array) <= k:
                        max_len = max(right - left, max_len)
                        break
        return max_len


# "AABABBA"  2
#  L
#   R
# [A:1,]
# 1

# create left and right pointer
# start pointer at the start of the window
# while loop where it will run until the right is less than size of string
# create a an array of 26 elements representing all the characters
# this will keep tract of no of characters in the sliding window
# add right pointer element to array
# and increment the right pointer
# calculate how many characters we can replace in window
# size of window(right - left) - max(array)
# if this value is <= k then continue
# else remove left count and increment the left count keep doing until the value becomes valid again
