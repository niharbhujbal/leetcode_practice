# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ""
        while l1 is not None:
            n1 += str(l1.val)
            l1 = l1.next
        n1 = "0" + n1[::-1]
        n2 = ""
        while l2 is not None:
            n2 += str(l2.val)
            l2 = l2.next
        n2 = "0" + n2[::-1]

        final_no = int(n1) + int(n2)

        head = ListNode(-1)
        p1 = head
        for i in str(final_no)[::-1]:
            p1.next = ListNode(int(i))
            p1 = p1.next
        return head.next


# read the first no by using a while loop store it as a str
# do the same for second
# now convert into into to reverse string of both and get addition
# now convert in string and start the pointer from end and keep adiing to head
