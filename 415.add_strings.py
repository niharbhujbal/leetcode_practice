class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_int = 0
        for i in num1:
            num1_int = (num1_int * 10) + int(i)
        num2_int = 0
        for i in num2:
            num2_int = num2_int * 10 + int(i)
        print(num1_int, num2_int)
        return str(num1_int + num2_int)
