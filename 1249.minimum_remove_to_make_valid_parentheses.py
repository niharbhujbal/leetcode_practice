import collections
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = collections.deque()
        index_to_remove = set()
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")" and len(stack) > 0:
                stack.pop()
            elif char == ")" and len(stack) == 0:
                index_to_remove.add(index)

        index_to_remove = index_to_remove.union(set(stack))
        clean_str = ""
        for index, char in enumerate(s):
            if index in index_to_remove:
                continue
            clean_str += char
        return clean_str


# here the idea is to push (  into stack
# when ) appears pop ( from stack if the stack is empty then we should remove that )
# after the loop if there are any ) in the stack then we should remove those too
