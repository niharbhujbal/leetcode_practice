# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def distanceK(self, root, target, k: int):
        graph_node = collections.defaultdict(list)

        def dfs(root, parent):
            nonlocal graph_node
            if root is None:
                return
            if parent is not None:
                graph_node[root.val].append(parent)
            if root.left is not None:
                graph_node[root.val].append(root.left)
            if root.right is not None:
                graph_node[root.val].append(root.right)
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        ans = []

        def dfs_graph(target, dist, visiting):
            nonlocal k, ans, graph_node
            if target in visiting:
                return
            if dist == k:
                ans.append(target.val)
                return
            for neb in graph_node[target.val]:
                visiting.add(target)
                dfs_graph(neb, dist + 1, visiting)

        dfs_graph(target, 0, set())
        return ans
