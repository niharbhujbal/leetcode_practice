class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += "+"
        st = []
        num = 0
        op = "+"

        for i in s:
            if i.isdigit():
                num = (num * 10) + int(i)
            elif i in {"+", "-", "/", "*"}:
                num = int(num)
                if op == "+":
                    st.append(num)
                elif op == "-":
                    st.append(-num)
                elif op == "*":
                    st.append(st.pop() * num)
                elif op == "/":
                    st.append(int(float(st.pop()) / float(num)))
                num = 0
                op = i

        return sum(st)


# we create a stack and keep pushing the no with its sign
# when we encounter a multiplication or div sign just pop no from the stack
# do the operation and push it to stack
# we have to add + at the end so the last no is psuhed to stack
# at the end we just take the sume of no
