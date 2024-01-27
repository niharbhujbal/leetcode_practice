# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = ListNode(-1, head)
        p2 = head
        p3 = head
        for i in range(n):
            p3 = p3.next

        while p3 is not None:
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next

        if p1.next is head and p2.next is None:
            return None
        if p1.next is head:
            return p2.next
        p1.next = p2.next

        return head


# create two pointer p1 and p2
# for loop of range n
# p1 will go forward until the range
# after this the p2 pointer will initiate and we will need one more prev pointer
# while p1 is not none increment both pointers
# we found the nth element from the end
# now just assign pev.next = curr.next
# return the head

# [1, 2, 3, 4, 5]
#                 p1
#                 p2
