class Solution:
    def myAtoi(self, s: str) -> int:
        # skipping all the leading white spaces
        ind = 0
        while ind < len(s) and s[ind] == " ":
            ind += 1
        
        # check leading sign
        
        if ind < len(s) and s[ind] == "-":
            sign = -1
            ind += 1
        elif ind < len(s) and s[ind] == "+":
            sign = 1
            ind += 1
        else:
            sign = 1
        
        # then run is digit function and keep adding to number
        value = 0
        while ind < len(s) and s[ind].isdigit():
            value = value * 10 + int(s[ind])
            ind += 1
        
        # if passed invalid values
        if value == 0:
            return value

        # to handle edge cases
        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31) - 1
        signed_value = sign * value
        if signed_value <= INT_MIN:
            return INT_MIN
        if signed_value >= INT_MAX:
            return INT_MAX
        
        return signed_value