class Solution:
    def partition(self, s):
        final_list = []

        def dfs(res, p):
            nonlocal s
            if p >= len(s):
                final_list.append(res)

            for length in range(1, len(s[p:]) + 1):
                string = s[p : p + length]
                if string == string[::-1]:
                    dfs(list(res + [string]), p + length)

        dfs([], 0)
        return final_list


# here we want to keep a pointer and keep increasing possible length of string from that point
# call the function if the string is a palindrome
# when you make all the possible combinations return the list
