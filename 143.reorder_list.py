# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        main_list = []
        while head is not None:
            main_list.append(head)
            head = head.next
        p1 = 0
        p2 = len(main_list) - 1
        merged_list = ListNode(0)
        p3 = merged_list
        while p1 <= p2:
            if p1 <= p2:
                p3.next = main_list[p1]
                p3 = p3.next
                p1 += 1
            if p1 < p2:
                p3.next = main_list[p2]
                p3 = p3.next
                p2 -= 1
        p3.next = None

        return merged_list.next

# store all the values in the list and iterate over the values n that order