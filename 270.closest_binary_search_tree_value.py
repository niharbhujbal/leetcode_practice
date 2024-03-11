# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root, target):
        min_dist, min_value = float("inf"), float("inf")

        def dfs(root):
            nonlocal target, min_dist, min_value
            if root is None:
                return

            dist = abs(root.val - target)
            if dist < min_dist:
                min_dist, min_value = dist, root.val
            elif dist == min_dist:
                min_value = min(root.val, min_value)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return min_value
