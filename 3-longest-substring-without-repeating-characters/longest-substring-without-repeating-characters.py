class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0

        max_len = 0
        for r in range(len(s)):
            if s[r] in hashmap and hashmap[s[r]] >= l:
                l = hashmap[s[r]] + 1
            hashmap[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len