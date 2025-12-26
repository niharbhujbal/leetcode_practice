# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        slow = head
        fast = head

        # Phase 1: Detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            # No cycle
            return None

        # Phase 2: Find entry point
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow