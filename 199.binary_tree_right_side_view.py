class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        level_order = self.level_order_traversal(root, [], 0)
        return [i[-1] for i in level_order]

    def level_order_traversal(self, root, nodes, level):
        if root is None:
            return nodes
        if level == len(nodes):
            nodes.append([])
        nodes[level].append(root.val)
        nodes = self.level_order_traversal(root.left, nodes, level + 1)
        nodes = self.level_order_traversal(root.right, nodes, level + 1)
        return nodes
