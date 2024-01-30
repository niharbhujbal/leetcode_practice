class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = []

        def dfs(node):
            if node is None:
                return False
            equality = p.val == node.val or q.val == node.val
            left = dfs(node.left)
            right = dfs(node.right)
            # any of the condition means that node is parent
            if (left and right) or (left and equality) or (right and equality):
                if len(ans) == 0:
                    ans.append(node)
            return equality or left or right

        dfs(root)
        return ans[0]


# here we will do the depth first search on the tree and our aim is get find the paths that have both the nodes
# if the path reachs eand and it never find the node the return false
# if it find any of the node then return true
# which has three condition either the itself or any of its childeren have that node
# when any two of those there conditions meet we have the answer node
