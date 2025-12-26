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
        def reverse_ll(prev,head,next_):
            head.next = prev
            if next_ is None:
                return head
            else:
                return reverse_ll(head,next_,next_.next)
        return reverse_ll(None,head,head.next)

            
