# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.good_nodes(root.val, root, 0)

    def good_nodes(self, max_val, root, count):
        if root is None:
            return count
        if root.val >= max_val:
            count += 1
            max_val = root.val
        count = self.good_nodes(max_val, root.left, count)
        count = self.good_nodes(max_val, root.right, count)
        return count
