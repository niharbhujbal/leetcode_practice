# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
    
        if head is None or head.next is None:
            return head

        odd_tail = head
        even_head = head.next
        even_tail = even_head
        
        while even_tail is not None and even_tail.next is not None:
            odd_tail.next = even_tail.next      
            odd_tail = odd_tail.next           

            even_tail.next = odd_tail.next     
            even_tail = even_tail.next         
        odd_tail.next = even_head               
        return head
        
