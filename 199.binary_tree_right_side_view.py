import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level_order = self.level_order_traversal(
            root, collections.defaultdict(list), 0
        ).values()
        return [i[-1] for i in level_order]

    def level_order_traversal(self, root, nodes, level):
        if root is None:
            return nodes

        nodes[level].append(root.val)
        nodes = self.level_order_traversal(root.left, nodes, level + 1)
        nodes = self.level_order_traversal(root.right, nodes, level + 1)
        return nodes
