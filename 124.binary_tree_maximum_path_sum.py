# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val = -1001
        max_val, max_sum = self.post_order_traversal(root, max_val)
        return max_sum

    def post_order_traversal(self, root, max_val):
        if root is None:
            return 0, max_val
        left, max_val = self.post_order_traversal(root.left, max_val)
        right, max_val = self.post_order_traversal(root.right, max_val)
        return max(left + root.val, right + root.val), max(
            max_val,
            left + right + root.val,
            root.val,
            right + root.val,
            left + root.val,
        )

# here we save max value from left and max value from right
# and save max sum every time