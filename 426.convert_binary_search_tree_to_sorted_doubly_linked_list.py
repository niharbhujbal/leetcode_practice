class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        head = Node(-1)
        current = head

        def dfs(node):
            nonlocal current
            if node is None:
                return None
            dfs(node.left)
            next_ = Node(node.val, left=current)
            current.right = next_
            current = next_
            dfs(node.right)

        dfs(root)
        last_node = current
        last_node.right = head.right
        current = current.right
        current.left = last_node

        return current


# if the the root node of tree is None then return none
# we know that if we do in order traversal then we get ascending order of the list
# so we have to traverse tree in that order
# we creat a head node with -1 value and sore the value in current node
# keep create the doubly link list and at the end we just complete the loop
