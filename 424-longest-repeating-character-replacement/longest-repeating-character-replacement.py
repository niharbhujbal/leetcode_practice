class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        array = [0] * 26
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            array[ord(s[right]) - ord('A')] += 1
            right += 1
            if right - left - max(array) <= k:
                max_len = max(right-left,max_len)
                continue
            else:
                while left < right:
                    array[ord(s[left]) - ord('A')] -= 1
                    left += 1
                    if right - left - max(array) <= k:
                        max_len = max(right-left,max_len)
                        break
        return max_len