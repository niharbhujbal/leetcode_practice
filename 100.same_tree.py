class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# terminating condition is when both of the nodes are nones means the value of p & q matches
# if one of the node is none then return false means the nodes do not match
# at the end we just want to check if the values match and left and right tree are same
