class Solution:
    def decodeString(self, s: str) -> str:
        no_stack = []
        char_stack = []
        current_no = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                current_no =  current_no * 10 + int(char)
            elif char == "[":
                no_stack.append(current_no)
                char_stack.append(current_string)
                current_no = 0
                current_string = ""
            elif char == "]":
                a = char_stack.pop()
                am = no_stack.pop()
                current_string = a + current_string * am
                
            else:
                current_string += char

        return current_string
