# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:

    def cloneGraph(self, node):
        if not node:
            return node
        hashmap = {}

        def dfs(node):
            if node is not None and node.val not in hashmap:
                hashmap[node.val] = Node(node.val)
                for n_node in node.neighbors:
                    dfs(n_node)
                    hashmap[node.val].neighbors.append(hashmap[n_node.val])

        dfs(node)
        ans = list(hashmap.values())
        if len(ans) == 0:
            return []
        else:
            return list(hashmap.values())[0]
