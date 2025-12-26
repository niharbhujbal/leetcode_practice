# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengtha = 0
        head = headA
        while head is not None:
            lengtha += 1
            head = head.next
        lengthb = 0
        head = headB
        while head is not None:
            lengthb += 1
            head = head.next
        
        # move pointer we have extra nodes
        heada = headA
        headb = headB
        if lengthb > lengtha:
            for _ in range(lengthb - lengtha):
                headb = headb.next
        elif lengtha > lengthb:
            for _ in range(lengtha - lengthb):
                heada = heada.next
        
        while heada is not None and headb is not None:
            if heada == headb:
                return heada
            heada = heada.next
            headb = headb.next
            
        return None

