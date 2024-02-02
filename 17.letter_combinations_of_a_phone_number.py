class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        final_list = []

        def dfs(i, formed_string):
            if i == len(digits):
                final_list.append(formed_string)
                return
            for possible in hashmap[digits[i]]:
                dfs(i + 1, formed_string + possible)

        if len(digits) == 0:
            pass
        else:
            dfs(0, "")
        return final_list


# create a hashmap of digit to list of possible letters
# a final list of all possible combination
# now for every no we have all the possible leeter we can use
# create a dfs function
# function will take index as input and created string
# terminating condition will index == length of letter string
# now get the possible combination of the ith at the index from string for loop and call dfs function with created string and the possible combination
