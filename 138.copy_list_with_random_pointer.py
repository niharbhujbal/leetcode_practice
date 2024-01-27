# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        node_reg = {}
        prev_node = None
        orignal_node = head
        copy_node = Node(head.val)
        current_node = copy_node
        # index = 0
        node_reg[head] = current_node
        while head.next is not None:
            head = head.next
            prev_node = current_node
            current_node = Node(head.val)
            # index += 1
            node_reg[head] = current_node
            prev_node.next = current_node
        head = orignal_node
        current_node = copy_node
        # index = 0
        while head is not None:
            if head.random is not None:
                current_node.random = node_reg[head.random]
            head = head.next
            current_node = current_node.next
            # index += 1
        return copy_node
