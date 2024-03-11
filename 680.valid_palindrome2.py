class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h, t = 0, len(s) - 1  # head and tail
        while h < t:
            if s[h] != s[t]:  # delete s[h] or s[t] and validate palindrome finally
                return (
                    s[h + 1 : t + 1] == s[h + 1 : t + 1][::-1] or s[h:t] == s[h:t][::-1]
                )
            h, t = h + 1, t - 1
        return True


# palindrome we can compare first letter and last letter of the string
# if they match then jast reduce the window
# if they don't match then either of the condition should be true
# remaining string should be palindrome or
# it should be palindrome if we leave one letter out from left or right
