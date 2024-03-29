import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = collections.defaultdict(list)
        return self.level_order_traversal(root, nodes, 0).values()

    def level_order_traversal(self, root, nodes, level):
        if root is None:
            return nodes

        nodes[level].append(root.val)

        nodes = self.level_order_traversal(root.left, nodes, level + 1)
        nodes = self.level_order_traversal(root.right, nodes, level + 1)
        return nodes


# lets taverse the tree in depth first order and note the
# return none if root node is none
# we will create a dictonary that will store the values of all the nodes
# as will call the next level we will keep incremeneting the level
# so we will need to check if the level is already present in the list or else we will add it to list
