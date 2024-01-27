# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        if curr is None:
            return None
        while curr.next is not None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        curr.next = prev
        return curr


# to reverse a linked list we need three pointers previous, current, next
# intialise with head in prevcurrent with next element
# while loop with condition next of previous should not be none
# get next of current in next
# then swap the prev and next
# then just shift all of them by one
#     1 <- 2 -> 3 -> 4 -> 5
#                    p    c    n
#
