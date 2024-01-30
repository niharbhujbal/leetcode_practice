# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        total = 0

        def dfs(root):
            if root is None:
                return None
            nonlocal total, low, high

            if root.val > low:
                dfs(root.left)
            if low <= root.val <= high:
                total += root.val
            if root.val < high:
                dfs(root.right)

        dfs(root)
        return total


# we do a depth first seach on tree to find out the total sum
# if the root value is less than low the there is no point in going to further left so we avoid that
# same with high
