class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        # null condition
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        prev_node = head
        current_node = head.next
        insert_node = False
        while True:
            # normal condition the element is between elements
            if prev_node.val <= insertVal <= current_node.val:
                break
            # it has to be inserted between head and tail
            if prev_node.val > current_node.val:
                if (insertVal < prev_node.val and insertVal <= current_node.val) or (
                    insertVal >= prev_node.val and insertVal > current_node.val
                ):
                    break
            prev_node = current_node
            current_node = current_node.next
            if prev_node == head:
                break
        # no value was inserted after loop
        insert_node = Node(insertVal)
        prev_node.next = insert_node
        insert_node.next = current_node
        return head
