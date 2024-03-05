class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []

        for log in logs:
            process_id, process, index = log.split(":")
            process_id = int(process_id)
            index = int(index)

            if process == "start":
                if len(stack) != 0:
                    stack_top_p_id, stack_top_i = stack[-1]
                    ans[stack_top_p_id] += index - stack_top_i
                stack.append([process_id, index])
            else:
                stack_top_p_id, stack_top_i = stack.pop()
                ans[stack_top_p_id] += index - stack_top_i + 1
                if len(stack) > 0:
                    stack[-1][-1] = index + 1
        return ans


# we can solve problem with a stack
# if type is start then push it to stack with index if stack is empty
# if it has elements then get element from stack and subtract it from index and add it to list
