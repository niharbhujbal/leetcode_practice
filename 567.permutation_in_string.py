import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        left = 0
        right = len(s1)
        s1_hm = collections.defaultdict(int)
        for i in s1:
            s1_hm[i] += 1
        s2_hm = collections.defaultdict(int)
        for i in s2[left:right]:
            s2_hm[i] += 1
        while right <= len(s2):
            if s1_hm == s2_hm:
                return True
            elif right == len(s2):
                break
            else:
                s2_hm[s2[left]] -= 1
                if s2_hm[s2[left]] == 0:
                    del s2_hm[s2[left]]
                left += 1
                if right <= len(s2):
                    s2_hm[s2[right]] += 1
                right += 1
        return False

                    

# set the size of window to size of the first string
# create hash map of both s1 and window of s2
# the keep incrementing both the pointers
# run a while loop until right is less than equal to length of s2
# compare the two hashmaps and if same then return true
# decrement the left pointer char and incrememnt it if its zero then delete it from dict
# add the right char then increment the right char