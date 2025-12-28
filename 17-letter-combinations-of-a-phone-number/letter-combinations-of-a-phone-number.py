class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}
        final_list = []

        def dfs(i, formed_string):
            if i == len(digits):
                final_list.append(formed_string)
                return
            for possible in hashmap[digits[i]]:
                dfs(i+1,formed_string+possible)
        
        if len(digits) == 0:
            pass
        else:
            dfs(0, '')
        return final_list
            