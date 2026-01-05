from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(arr)
        prev_less_index = [-1] * n
        next_less_or_equal_index = [n] * n

        # Pass 1: previous strictly less (<)
        increasing_stack: List[int] = []
        for i in range(n):
            while increasing_stack and arr[increasing_stack[-1]] >= arr[i]:
                increasing_stack.pop()
            prev_less_index[i] = increasing_stack[-1] if increasing_stack else -1
            increasing_stack.append(i)

        # Pass 2: next less-or-equal (<=), scan from right
        increasing_stack.clear()
        for i in range(n - 1, -1, -1):
            while increasing_stack and arr[increasing_stack[-1]] > arr[i]:
                increasing_stack.pop()
            next_less_or_equal_index[i] = increasing_stack[-1] if increasing_stack else n
            increasing_stack.append(i)

        total = 0
        for i in range(n):
            left_choices = i - prev_less_index[i]
            right_choices = next_less_or_equal_index[i] - i
            contribution = (arr[i] * left_choices * right_choices) % MOD
            total = (total + contribution) % MOD

        return total

    
# we want to count how many time min contribution occurs from specific element
# for that we need what is prev min ele ind with no found as -1
# nex next smaller ele index with no found as length of array
# at the difference between index and the ans and multiply the differences
# -1 -1 1  1
# 1  4 4 4
# 4, 3, 2, 1