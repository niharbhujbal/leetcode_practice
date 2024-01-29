class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if (
            p.val < root.val < q.val
            or p.val > root.val > q.val
            or root.val == p.val
            or root.val == q.val
        ):
            return root
        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)


# try to solve the problem with reccursion
# so our last condition which will end reccursion is
# first we will make sure p is smaller and q is bigger
# then if the value of root is in between p and q or any of the value is equal to root val
# then return the root value
# if both the value is less tha root then call the same function with left node as root
# if booth the nodes are bigger then call the fnction with right node
