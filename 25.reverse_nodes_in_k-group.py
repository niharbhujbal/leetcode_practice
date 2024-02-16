# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        prehead = ListNode(-1, head)
        group_prev = prehead

        def get_kth_node(node, k):
            while node is not None and k > 0:
                node = node.next
                k -= 1
            return node

        while True:
            kth_node = get_kth_node(group_prev, k)
            if kth_node is None:
                break
            groupNext = kth_node.next

            prev, curr = kth_node.next, group_prev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp
        return prehead.next


# we start with the pre head
# the few pointer pointing prev of group and next of group after kth node
# point first node of group to group next and group prev to kth node
# and reverse the group
# if kth node is node
# then just break out of the loop
