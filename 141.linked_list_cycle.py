class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # in floyd's algorithm we are  we will have one slow pointer and one fast pointer
        # slow will move one place at a time and fast will move tow places at the time# if fast reaches None then the algorithm dosent has cycle
        # but if the pointer meet then the algorithm has cycle
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
