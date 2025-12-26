# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        
        prev = None
        curr = head

        while curr.next is not None :
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            nex = curr.next
        curr.next = prev
        return curr
            
