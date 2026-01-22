class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits_stack: List[str] = []

        for digit in num:
            while k > 0 and digits_stack and digits_stack[-1] > digit:
                digits_stack.pop()
                k -= 1
            digits_stack.append(digit)

        # If still need to remove digits, remove from end (least significant positions).
        while k > 0 and digits_stack:
            digits_stack.pop()
            k -= 1

        result = "".join(digits_stack).lstrip("0")
        return result if result != "" else "0"
            